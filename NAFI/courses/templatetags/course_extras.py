from django import template
from courses.models import UserProgress

register = template.Library()

@register.filter(name='check_lesson_progress')
def check_lesson_progress(lesson, user):
    try:
        progress = UserProgress.objects.get(user=user, lesson=lesson)
        return progress.completed
    except UserProgress.DoesNotExist:
        return False
    