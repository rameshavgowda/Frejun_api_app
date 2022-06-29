from django.shortcuts import render
from .models import Task, Team
from .serializers import TeamSerializer,TaskSerializer,TaskstatusSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from .pagination import Mypagepagination
from Api.task import mail_fun
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class CreateTeam(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser] 

class CreateTask(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    mail_fun()

class UpdateTask(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

class ListTask(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = Mypagepagination
    authentication_classes = [SessionAuthentication]
    permission_classes = [AllowAny]

class Updatestatus(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskstatusSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
        
