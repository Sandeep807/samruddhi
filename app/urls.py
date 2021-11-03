from django.urls import path
from .views import *
urlpatterns = [
    path('register/',CustomerView.as_view()),
    path('login/',LoginView.as_view()),
    path('balance/',Balance.as_view()),
    path('aproved/',StatusAproved.as_view()),
    path('reject/',StatusReject.as_view()),
    path('allcustomer/',AllCustomer.as_view()),
    path('allagent/',AllAgent.as_view()),
    path('goldprice/',GetGoldPrice.as_view())
]
