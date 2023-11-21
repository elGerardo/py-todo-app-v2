from django.urls import path
from .views import *

urlpatterns = [
    path("todo/task/<str:task_id>/step/<str:step_id>", Step_ApiView_Detail.as_view()),
]
