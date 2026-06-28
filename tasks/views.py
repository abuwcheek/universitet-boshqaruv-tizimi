from django.shortcuts import render

from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from .serializers import TeacherTaskStatusSerializer

from .services import get_task_queryset



class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return get_task_queryset(
            self.request.user
        )



class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return get_task_queryset(
            self.request.user
        )



class TeacherTaskStatusAPIView(generics.UpdateAPIView):
    serializer_class = TeacherTaskStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            employee=self.request.user
        )



class MyTaskListAPIView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(
            employee=self.request.user
        )