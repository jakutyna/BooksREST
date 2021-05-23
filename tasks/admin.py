# I've added Django admin for manual testing
from django.contrib import admin

from .models import Account, Book, Operation, Purchase

admin.site.register(Operation)
admin.site.register(Purchase)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')


@admin.register(Account)
class BookAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'balance')
