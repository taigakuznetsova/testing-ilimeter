from django.urls import path
from .views import CustomSignupView, CustomLoginView, CustomLogoutView, profile, edit_profile

app_name = 'users'

urlpatterns = [
    path('register/', CustomSignupView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]