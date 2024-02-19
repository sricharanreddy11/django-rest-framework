from django.urls import path, include
from rest_framework import routers

from django.contrib import admin
from core.views import (
    UserViewSet,
    StudentViewSet,
    DepartmentViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# Serializers define the API representation.


# ViewSets define the view behavior.


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('students', StudentViewSet)
router.register('departments', DepartmentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # JWT Auth URLs
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]