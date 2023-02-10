from django.forms import ModelForm
from .models import Account, Transaction

# create Account Form based on Account model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

# create Transaction Form based on Transaction model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'