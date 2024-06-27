from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/complete/', views.mark_lesson_completed, name='mark_lesson_completed'),
    path('lesson/<int:lesson_id>/incomplete/', views.unmark_lesson_completed, name='unmark_lesson_completed'),
    path('my-courses/', views.user_courses, name='user_courses'),
    path('access-denied/', views.access_denied, name='access_denied'),
]
