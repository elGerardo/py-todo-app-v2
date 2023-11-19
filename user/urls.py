from django.urls import path
from .views import *

urlpatterns = [
    path("todo/user", User_ApiView.as_view()),
    path("todo/user/login", User_ApiView_Details.login),
    path("todo/user/<str:user_id>", User_ApiView_Details.as_view()),
]
