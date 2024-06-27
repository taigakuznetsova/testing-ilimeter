from django.urls import path
from .views import create_report

app_name = 'reports'

urlpatterns = [
    path('create/', create_report, name='create_report'),
]
