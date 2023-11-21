from rest_framework.views import APIView
from todoapp.helpers.get_access_token import GetAccessToken
from rest_framework.permissions import IsAuthenticated
from .models import Step
from task.models import Task
from django.shortcuts import get_object_or_404
from .serializer import StepSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

# Create your views here.
class Step_ApiView_Detail(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, task_id, step_id):
        GetAccessToken(request.headers.get("Authorization", None))
        task = get_object_or_404(Task, id=task_id)
        step = get_object_or_404(Step, id=step_id)

        body = {**request.data, "task": task.id, "id": step.id}

        serializer = StepSerializer(step, data=body)
        if serializer.save():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, task_id, step_id):
        GetAccessToken(request.headers.get("Authorization", None))
        get_object_or_404(Task, id=task_id)
        step = get_object_or_404(Step, id=step_id)
        step.delete()
        return JsonResponse({"message": "Row deleted"}, status=status.HTTP_202_ACCEPTED)