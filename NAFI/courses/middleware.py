from django.shortcuts import redirect
from django.urls import reverse
from courses.models import Lesson, UserCourse

class LessonAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if 'lesson_id' in view_kwargs:
            lesson_id = view_kwargs['lesson_id']
            try:
                lesson = Lesson.objects.get(id=lesson_id)
                course = lesson.module.course
                user = request.user
                if not UserCourse.objects.filter(user=user, course=course).exists():
                    return redirect(reverse('access_denied'))
            except Lesson.DoesNotExist:
                pass
        return None
