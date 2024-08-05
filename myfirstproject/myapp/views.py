from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer


class HelloWorldView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello, World!"}, status=status.HTTP_200_OK)

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
