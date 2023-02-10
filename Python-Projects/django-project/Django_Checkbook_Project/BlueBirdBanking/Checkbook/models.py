from django.db import models

# Create your models here.

# Create Account model
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # defines the model Manager for Accounts
    Accounts = models.Manager()

    # allows references to specific account be returned as owner's name, not primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Choices for transaction
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal','Withdrawal')]

# Create Transaction model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()