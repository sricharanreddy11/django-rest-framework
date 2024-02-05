# from django.shortcuts import render
from core.models import (
    Student,
    Department,
)
from django.contrib.auth.models import User
from core.serializers import (
    UserSerializer,
    StudentSerializer,
    DepartmentSerializer,
)
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
