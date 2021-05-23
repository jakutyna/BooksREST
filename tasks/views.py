from django.db.models import Sum
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account, Book, Purchase, Operation
from .serializers import BookSerializer, PurchaseSerializer
from .utils import spend_money


# Generic view used for simplicity
class BookListView(ListAPIView):
    """View for listing books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class PurchaseView(APIView):
    """View for buying books"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = PurchaseSerializer(data=data)
        if serializer.is_valid():
            account = Account.objects.get(user=request.user)

            # Filter all books from request data
            books = Book.objects.filter(id__in=serializer.data["books"])
            # Calculate total cost of books
            total_cost = round(books.aggregate(Sum('price'))['price__sum'], 2)

            # Checking and updating account balance
            try:
                spend_money(account, total_cost)
            except ValueError:
                return Response({"detail": "Insufficient funds"}, status=status.HTTP_402_PAYMENT_REQUIRED)

            # Create Purchase model instance and save it to db
            purchase = Purchase(account=account, total_cost=total_cost)
            purchase.save()
            purchase.books.set(books)
            purchase.save()

            # Adding entry about purchase to Operation table
            Operation.objects.create(operation_type=Operation.PURCHASE, balance_change=total_cost,
                                     current_balance=account.balance, account=account)

            # Required response schema is different from request - response created manually (no serializer used)
            response_dict = dict(serializer.data)
            response_dict["total_cost"] = total_cost
            return Response(response_dict)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
