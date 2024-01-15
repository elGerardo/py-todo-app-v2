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
        body = {**request.data, "user": token.access_token["user_id"]}

        step_fields = None
        if 'steps' in body:
            step_fields = body['steps']

        task_serializer = TaskSerializer(data=body, step_fields=step_fields)
        if task_serializer.is_valid():
            task = task_serializer.save()
            if isinstance(task, Task) == False:
                return Response(task, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        return Response(task_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request):
        search = request.GET.get('search', None)
        
        token = GetAccessToken(request.headers.get("Authorization", None))
        
        if search is not None:
            tasks = Task.objects.filter(user=token.access_token["user_id"]).filter(title__icontains=search)
        else:
            tasks = Task.objects.filter(user=token.access_token["user_id"])

        serializer = TaskSerializer(tasks, many=True)
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
        body = {**request.data, "user": token.access_token["user_id"]}
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