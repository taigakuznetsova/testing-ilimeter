from django.urls import path
from . import views

urlpatterns = [
    path('statistics/', views.statistics, name='statistics'),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),
    path('manage/<int:department_id>/', views.manage_department, name='manage_department'),
]
