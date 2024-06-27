from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Module, Lesson, UserCourse, UserProgress
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user_course = None
    if request.user.is_authenticated:
        user_course = course.usercourse_set.filter(user=request.user).first()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'user_course': user_course
    })


@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    user_course, created = UserCourse.objects.get_or_create(user=request.user, course=course)
    return redirect('course_detail', course_id=course.id)


@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    user_progress = None

    if request.user.is_authenticated:
        user_progress = UserProgress.objects.filter(lesson=lesson, user=request.user).first()

    previous_lesson = None
    next_lesson = None

    all_modules = list(lesson.module.course.modules.all())
    all_lessons_in_course = [lesson for module in all_modules for lesson in module.lessons.all()]
    current_lesson_index = all_lessons_in_course.index(lesson)

    if current_lesson_index > 0:
        previous_lesson = all_lessons_in_course[current_lesson_index - 1]
    if current_lesson_index + 1 < len(all_lessons_in_course):
        next_lesson = all_lessons_in_course[current_lesson_index + 1]

    return render(request, 'courses/lesson_detail.html', {
        'lesson': lesson,
        'user_progress': user_progress,
        'previous_lesson': previous_lesson,
        'next_lesson': next_lesson
    })


@login_required
def user_courses(request):
    user_courses = UserCourse.objects.filter(user=request.user)
    return render(request, 'courses/user_courses.html', {'user_courses': user_courses})


@login_required
def mark_lesson_completed(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    user_progress, created = UserProgress.objects.get_or_create(user=request.user, lesson=lesson)

    if not user_progress.completed:
        user_progress.completed = True
        user_progress.completed_at = timezone.now()
        user_progress.save()

        course = lesson.module.course
        if course.all_lessons_completed(request.user):
            user_course = UserCourse.objects.get(user=request.user, course=course)
            user_course.completed_at = timezone.now()
            user_course.save()
            messages.success(request, 'Поздравляем! Вы завершили курс.')
            return redirect('user_courses')

        next_lesson = None
        all_lessons = list(lesson.module.lessons.all())
        current_index = all_lessons.index(lesson)

        if current_index + 1 < len(all_lessons):
            next_lesson = all_lessons[current_index + 1]
        else:
            all_modules = list(lesson.module.course.modules.all())
            current_module_index = all_modules.index(lesson.module)

            if current_module_index + 1 < len(all_modules):
                next_module = all_modules[current_module_index + 1]
                next_lesson = next_module.lessons.first()
                messages.success(request, f'Вы завершили модуль. Переход к следующему модулю {next_module.title}.')

        if next_lesson:
            return redirect('lesson_detail', lesson_id=next_lesson.id)
        else:
            return redirect('course_detail', course_id=lesson.module.course.id)
    else:
        messages.info(request, 'Этот урок уже завершен.')
        return redirect('lesson_detail', lesson_id=lesson.id)


@login_required
def unmark_lesson_completed(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    try:
        user_progress = UserProgress.objects.get(user=request.user, lesson=lesson)
        if user_progress.completed:
            user_progress.completed = False
            user_progress.completed_at = None
            user_progress.save()

            course = lesson.module.course
            user_course = UserCourse.objects.get(user=request.user, course=course)
            user_course.completed_at = None
            user_course.save()

            messages.success(request, 'Урок отмечен как незавершенный. Статус курса обновлен.')
    except UserProgress.DoesNotExist:
        messages.error(request, 'Прогресс по этому уроку не найден.')
    return redirect('lesson_detail', lesson_id=lesson.id)


def access_denied(request):
    return render(request, 'courses/access_denied.html')