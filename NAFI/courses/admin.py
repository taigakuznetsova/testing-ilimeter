from django.contrib import admin
from .models import Course, Module, Lesson, UserCourse, UserProgress

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]
    list_display = ('title', 'is_free')
    search_fields = ('title', 'description')

class ModuleAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('title', 'course')
    search_fields = ('title', 'description')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module')
    search_fields = ('title', 'content')

class UserCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'enrolled_at', 'completed_at')
    search_fields = ('user__username', 'course__title')

class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed_status')
    search_fields = ('user__username', 'lesson__title')

admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(UserCourse, UserCourseAdmin)
admin.site.register(UserProgress, UserProgressAdmin)
