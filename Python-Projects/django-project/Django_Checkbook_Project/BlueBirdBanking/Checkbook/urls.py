from django.urls import path
from . import views

urlpatterns = [
    # set url path to home page index.html
    path('', views.home, name='index'),
    # set Create New Account url
    path('create/', views.create_account, name='create'),
    # set Balance Sheet url
    path('<int:pk>balance/', views.balance, name='balance'),
    # set Add New Transaction url
    path('transaction/', views.transaction, name='transaction')
]