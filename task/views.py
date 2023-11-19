from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializer import TaskSerializer
from rest_framework.response import Response
from .models import Task
from todoapp.helpers.get_access_token import GetAccessToken
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.
class Task_ApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token = GetAccessToken(request.headers.get("Authorization", None))
        body = {**request.data, "user_id": token.access_token["user_id"]}

        serializer = TaskSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request):
        token = GetAccessToken(request.headers.get("Authorization", None))
        task = Task.objects.filter(user_id=token.access_token["user_id"])
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class Task_ApiView_Detail(APIView):
    permission_classes = (IsAuthenticated,)

    #find
    def get(self, request, task_id):
        GetAccessToken(request.headers.get("Authorization", None))
        task = get_object_or_404(Task, id=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, task_id):
        token = GetAccessToken(request.headers.get("Authorization", None))
        task = get_object_or_404(Task, id=task_id)
        body = {**request.data, "user_id": token.access_token["user_id"]}
        serializer = TaskSerializer(task, data=body)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, task_id):
        GetAccessToken(request.headers.get("Authorization", None))
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({"message": "Row deleted"}, status=status.HTTP_202_ACCEPTED)