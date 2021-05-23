from django.db import models


class Account(models.Model):
    """
    Account model holds current balance of every user.
    """
    balance = models.DecimalField(max_digits=8, decimal_places=2)

    # Default Django User model used
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    @property
    def account_name(self):
        return f'{self.user.username}\'s account'

    def __str__(self):
        return self.account_name


class Operation(models.Model):
    """
    Each change (deposit, purchase, etc..) of Account's balance should be reflected
    in the Operation model for auditing purposes.
    """
    DEPOSIT = 'DP'
    PURCHASE = 'PC'

    OPERATION_TYPE_CHOICES = (
        (DEPOSIT, 'deposit'),
        (PURCHASE, 'purchase')
    )

    # Two operation types were assumed for the purpose of this task: deposit, purchase
    operation_type = models.CharField(choices=OPERATION_TYPE_CHOICES, max_length=2)

    # Value of change in the account's balance
    balance_change = models.DecimalField(max_digits=8, decimal_places=2)

    # Balance on the account after the operation
    current_balance = models.DecimalField(max_digits=8, decimal_places=2)

    # Operation date
    created_at = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Book(models.Model):
    """
    Model stores a title of the book and its price.
    """
    title = models.CharField(max_length=128)

    # Assumed that all fields representing currency have 2 decimal places
    # 8 digits should be enough for books prices :)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title


class Purchase(models.Model):
    """
    Model stores data about purchases.
    """

    total_cost = models.DecimalField(max_digits=8, decimal_places=2)

    # Book ids for each purchase will be stored in the intermediate table.
    # TODO: Create custom class for intermediate table with field 'amount'
    # TODO: allowing to buy multiple copies of specific book at once.
    books = models.ManyToManyField(Book)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
