from django.urls import path
from .views import *
urlpatterns = [
    path('register/',CustomerView.as_view()),
    path('login/',LoginView.as_view()),
]
