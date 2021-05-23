from rest_framework import generics, permissions

from .models import Book
from .serializers import BookSerializer


# Generic view used for simplicity
class BookListView(generics.ListAPIView):
    """Book list View"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
