from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, UserProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'user-profiles', UserProfileViewSet, basename='userprofile')

urlpatterns = router.urls