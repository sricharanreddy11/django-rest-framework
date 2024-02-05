from rest_framework import serializers
from core.models import (
    Student,
    Department,
)
from django.contrib.auth.models import User


class StudentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Student
        fields = ['url', 'student_id', 'student_name', 'student_age', 'student_email', 'cgpa', 'address', 'department']


class DepartmentSerializer(serializers.ModelSerializer):
    # students = serializers.StringRelatedField(many=True)
    # students = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='student-detail')
    # students = serializers.SlugRelatedField(many=True, read_only=True, slug_field='student_name')
    # students = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='student-detail')
    # students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['department_id', 'department_name', 'students']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
