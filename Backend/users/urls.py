from django.contrib import admin
from django.urls import path, include
from . import views
from .views import RegisterView, LoginView, UserView, LogoutView, DepositView, WithdrawView, TransactionListView, SendView

urlpatterns =[
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('user/',UserView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('deposit/',DepositView.as_view()),
    path('withdraw/',WithdrawView.as_view()),
    path('transactions/',TransactionListView.as_view()),
    path('send/',SendView.as_view())
    ]