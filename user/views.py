from django.shortcuts import render
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

# Create your views here.
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
