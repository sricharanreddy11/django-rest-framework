from django.contrib import admin
from core.models import (
    Student,
    Department,
)

admin.site.register(Student)
admin.site.register(Department)

