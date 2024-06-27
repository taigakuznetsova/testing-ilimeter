from django.db import models
from django.conf import settings
from courses.models import Course


class Department(models.Model):
    name = models.CharField(max_length=255)
    head = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='headed_departments', on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='departments')
    courses = models.ManyToManyField(Course, related_name='departments', blank=True)

    def __str__(self):
        return self.name
    