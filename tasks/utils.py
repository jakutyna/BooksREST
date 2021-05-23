from rest_framework import status
from rest_framework.response import Response


def spend_money(account, total_cost):
    """
    Checks if the funds on account are sufficient to make a purchase.
    """
    if account.balance < total_cost:
        raise ValueError('Insufficient funds')
    account.balance -= total_cost
    account.save()
