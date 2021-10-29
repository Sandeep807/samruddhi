from django.urls import path
from .views import *
urlpatterns = [
    path('register/',CustomerView.as_view()),
    path('login/',LoginView.as_view()),
    path('balance/',Balance.as_view()),
    path('stat/',StatusView.as_view()),
    path('allcustomer/',AllCustomer.as_view()),
    path('allagent/',AllAgent.as_view()),
]
