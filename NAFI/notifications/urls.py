from django.urls import path
from . import views

urlpatterns = [
    path('my-notifications/', views.user_notifications, name='user_notifications'),
    path('read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
]
