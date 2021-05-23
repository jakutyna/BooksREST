from django.urls import include, path

from .views import BookListView, PurchaseView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/buy/', PurchaseView.as_view(), name='buy-books'),
    # Default Django REST login/logout views used for authentication
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
