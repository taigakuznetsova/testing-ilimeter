from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_meeting, name='create_meeting'),
    path('meeting/<int:meeting_id>/', views.meeting_detail, name='meeting_detail'),
    path('<int:meeting_id>/edit/', views.edit_meeting, name='edit_meeting'),
    path('my_meetings/', views.user_meetings, name='user_meetings'),
    path('calendar/', views.calendar_view, name='calendar'),
]
