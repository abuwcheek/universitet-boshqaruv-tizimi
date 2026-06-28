from django.shortcuts import render

from rest_framework import generics

from .models import Department
from .serializers import DepartmentSerializer


class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer



class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer