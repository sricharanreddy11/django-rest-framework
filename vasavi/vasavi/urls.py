from django.urls import path, include
from rest_framework import routers
from core.views import (
    UserViewSet,
    StudentViewSet,
    DepartmentViewSet,
)


# Serializers define the API representation.


# ViewSets define the view behavior.


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('students', StudentViewSet)
router.register('departments', DepartmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]