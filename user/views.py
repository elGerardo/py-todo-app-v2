from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .serializer import UserSerializer
from .models import User
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from todoapp.helpers.get_access_token import GetAccessToken

# Create your views here.
class User_ApiView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class User_ApiView_Details(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, user_id):
        token = GetAccessToken(request.headers.get("Authorization", None))
        
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        GetAccessToken(request.headers.get("Authorization", None))
        
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(["POST"])
    def login(request):
        user = get_object_or_404(User, username=request.data.get("username"))
        if check_password(request.data.get("password", None), user.password):
            refresh = RefreshToken.for_user(user)
            return JsonResponse({"refresh": (str(refresh)), 'access': str(refresh.access_token)}, status=201)
        return JsonResponse({"message": "Username or Password Incorrect"}, status=401)
