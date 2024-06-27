from django.db import models
from django.conf import settings
from tinymce import models as tinymce_models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_free = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def all_lessons_completed(self, user):
        total_lessons = Lesson.objects.filter(module__course=self).count()
        completed_lessons = UserProgress.objects.filter(lesson__module__course=self, user=user, completed=True).count()
        return total_lessons == completed_lessons
    
    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.title} - {self.course}'

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField()
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_completed(self, user):
        progress, created = UserProgress.objects.get_or_create(user=user, lesson=self)
        progress.completed = True
        progress.completed_at = models.DateTimeField(auto_now=True)
        progress.save()

    def is_completed_by(self, user):
        progress = UserProgress.objects.filter(user=user, lesson=self).first()
        return progress.completed if progress else False

    def user_progress(self, user):
        progress = UserProgress.objects.filter(user=user, lesson=self).first()
        return progress if progress else None
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class UserCourse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class UserProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Progress'
        unique_together = ('user', 'lesson')  # Ensure one record per user and lesson

    def __str__(self):
        return f'{self.user.username} - {self.lesson.title}'

    @property
    def completed_status(self):
        return "Completed" if self.completed else "In Progress"