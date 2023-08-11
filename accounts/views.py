from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView, Response
from rest_framework import status

from accounts.serializers import UserSerializer


class RegisterAPI(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
