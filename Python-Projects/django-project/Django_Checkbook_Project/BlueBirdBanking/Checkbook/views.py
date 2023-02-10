from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# Create your views here.

# Fuction will render Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None) # Retrieve the Account form
    if request.method == 'POST': # Check if request is POST
        pk = request.POST['account'] # if form is submitted, retrieve which account user wants to view
        return balance(request, pk) # call balance function to render account's balance sheet
    content = {'form': form} # pass content to template in dictionary
    return render(request, 'checkbook/index.html', content) # add content to page

# Render Create New Account page
def create_account(request):
    form = AccountForm(data=request.POST or None) # Retrieve the Account form
    if request.method == 'POST': # Check if request is POST
        if form.is_valid(): # Check if submitted form is valid, if so, save
            form.save()
            return redirect('index') # Returns user to home page
    content = {'form': form} # Saves content to template as dictionary
    return render(request, 'checkbook/CreateNewAccount.html', content) # adds content of form to page

# render Balance page
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrieve the requested account using primary key
    transactions = Transaction.Transactions.filter(account=pk) # retrieve all of account's transactions
    current_total = account.initial_deposit # create account total variable
    table_contents = {} # create dictionary into which transaction information will be placed
    for t in transactions: # loop through transactions
        if t.type == 'Deposit':
            current_total += t.amount # if deposit, add amount to balance
            table_contents.update({t: current_total}) # add/update transaction and total to dictionary
        else:
            current_total -= t.amount # if withdrawal, subtract amount from balance
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total} # pass all the info to template and render
    return render(request, 'checkbook/BalanceSheet.html', content)

# render Transaction page
def transaction(request):
    form = TransactionForm(data=request.POST or None) # Retrieve the Account form
    if request.method == 'POST': # Check if request is POST
        if form.is_valid(): # Check if submitted form is valid, if so, save
            pk = request.POST['account']
            form.save()
            return balance(request,pk) # Returns user to home page
    content = {'form': form} # Saves content to template as dictionary
    return render(request, 'checkbook/AddTransaction.html', content)