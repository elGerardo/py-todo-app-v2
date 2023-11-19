from django.urls import path
from .views import *

urlpatterns = [
    path("todo/task", Task_ApiView.as_view()),
    path("todo/task/<str:task_id>", Task_ApiView_Detail.as_view()),
]
