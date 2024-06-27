from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from courses.models import UserCourse, Course, UserProgress
from django.contrib.auth.decorators import login_required
from .forms import DepartmentForm, AddMemberForm, AddCourseForm
from config.decorators.user_passes_test_custom import user_passes_test_custom
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.utils import timezone
from datetime import datetime, timedelta

User = get_user_model()


def is_department_head(user):
    return Department.objects.filter(head=user).exists()


def get_week_start_end():
    today = timezone.now().date()
    start_date = today - timedelta(days=today.weekday())
    end_date = start_date + timedelta(days=6)
    return start_date, end_date


@user_passes_test_custom(is_department_head)
@login_required
def manage_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    add_member_form = AddMemberForm()
    add_course_form = AddCourseForm()

    if request.method == 'POST':
        if 'add_members' in request.POST:
            add_member_form = AddMemberForm(request.POST)
            if add_member_form.is_valid():
                new_members = add_member_form.cleaned_data['new_members']
                department.members.add(*new_members)
        elif 'remove_member' in request.POST:
            member_id = request.POST.get('member_id')
            member = get_object_or_404(User, id=member_id)
            department.members.remove(member)
        elif 'add_courses' in request.POST:
            add_course_form = AddCourseForm(request.POST)
            if add_course_form.is_valid():
                new_courses = add_course_form.cleaned_data['new_courses']
                department.courses.add(*new_courses)
        elif 'remove_course' in request.POST:
            course_id = request.POST.get('course_id')
            course = get_object_or_404(Course, id=course_id)
            department.courses.remove(course)

    return render(request, 'departments/manage_department.html', {
        'department': department,
        'add_member_form': add_member_form,
        'add_course_form': add_course_form,
    })


@login_required
def statistics(request):
    departments = Department.objects.all()
    department_stats = []
    total_completed_lessons = 0
    total_learners = 0
    total_non_learners = 0

    start_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0),
    end_date = timezone.now().replace(hour=23, minute=59, second=59, microsecond=999999)

    period = request.GET.get('period', 'month')
    if period == 'day':
        start_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        end_date = timezone.now().replace(hour=23, minute=59, second=59, microsecond=999999)
    elif period == 'week':
        start_date, end_date = get_week_start_end()
        start_date = timezone.make_aware(datetime.combine(start_date, datetime.min.time()))
        end_date = timezone.make_aware(datetime.combine(end_date, datetime.max.time()))
    elif period == 'month':
        start_date = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        last_day = (timezone.now().replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        end_date = last_day.replace(hour=23, minute=59, second=59, microsecond=999999)
    elif period == 'year':
        start_date = timezone.now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        end_date = timezone.now().replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
    elif period == 'custom':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if not start_date or not end_date:
            start_date = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            end_date = timezone.now()
        else:
            start_date = timezone.make_aware(
                datetime.strptime(start_date, '%Y-%m-%d').replace(hour=0, minute=0, second=0, microsecond=0))
            end_date = timezone.make_aware(
                datetime.strptime(end_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59, microsecond=999999))
    else:
        start_date = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        last_day = (timezone.now().replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
        end_date = last_day.replace(hour=23, minute=59, second=59, microsecond=999999)

    for department in departments:
        courses = department.courses.all()
        members = department.members.all()
        total_members = members.count()
        learners = UserCourse.objects.filter(user__in=members).distinct('user').count()
        non_learners = total_members - learners
        total_learners += learners
        total_non_learners += non_learners

        department_completed_lessons = 0

        for course in courses:
            modules = course.modules.all()
            print(UserProgress.objects.filter(lesson__module__in=modules).values('completed_at').distinct().order_by(
                'completed_at'))
            completed_lessons = UserProgress.objects.filter(
                lesson__module__in=modules,
                user__in=department.members.all(),
                completed=True,
                completed_at__range=(start_date, end_date)
            ).count()
            department_completed_lessons += completed_lessons
        total_completed_lessons += department_completed_lessons

        department_stats.append({
            'department': department,
            'total_members': total_members,
            'learners': learners,
            'non_learners': non_learners,
            'department_completed_lessons': department_completed_lessons
        })

    context = {
        'departments': department_stats,
        'total_completed_lessons': total_completed_lessons,
        'total_learners': total_learners,
        'total_non_learners': total_non_learners,
        'period': period,
        'start_date': start_date,
        'end_date': end_date if period == 'custom' else None
    }

    return render(request, 'departments/statistics.html', context)


@login_required
def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    courses = department.courses.all()
    members = department.members.all()

    total_members = members.count()
    total_men = members.filter(userprofile__gender='M').count()
    total_women = members.filter(userprofile__gender='F').count()
    total_learners = total_men + total_women

    user_courses = UserCourse.objects.filter(user__in=members)
    enrolled_counts = user_courses.values('course').annotate(count=Count('id')).order_by('course')

    course_stats = []
    for course in courses:
        enrolled_count = enrolled_counts.filter(course=course.id).first()
        enrolled_count = enrolled_count['count'] if enrolled_count else 0

        completed_count = UserProgress.objects.filter(
            user__in=members,
            lesson__module__course=course,
            completed=True
        ).values('user').distinct().count()

        # не используется но может пригодится для графика
        total_lessons = course.modules.aggregate(total_lessons=Count('lessons'))['total_lessons']

        completed_percent = round((completed_count / total_members) * 100, 2) if total_members > 0 else 0

        course_stats.append({
            'course': course,
            'enrolled_count': enrolled_count,
            'completed_percent': completed_percent,
            'total_lessons': total_lessons
        })

    male_percentage = (total_men / total_members) * 100 if total_members > 0 else 0
    female_percentage = (total_women / total_members) * 100 if total_members > 0 else 0

    period = request.GET.get('period', 'month')
    if period == 'day':
        start_date = timezone.now().date()
    elif period == 'year':
        start_date = timezone.now().replace(month=1, day=1)
    elif period == 'custom':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        if not start_date or not end_date:
            start_date = timezone.now().replace(day=1)
            end_date = timezone.now()
        else:
            from django.utils.dateparse import parse_date
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
    else:
        from django.utils import timezone
        start_date = timezone.now().replace(day=1)

    if period != 'custom':
        end_date = timezone.now()

    lesson_completions = 0

    for course in courses:
        modules = course.modules.all()
        completed_lessons_count = UserProgress.objects.filter(
            lesson__module__in=modules,
            user__in=department.members.all(),
            completed=True
        ).count()
        lesson_completions += completed_lessons_count

    context = {
        'department': department,
        'total_members': total_members,
        'total_men': total_men,
        'total_women': total_women,
        'male_percentage': male_percentage,
        'female_percentage': female_percentage,
        'total_learners': total_learners,
        'course_stats': course_stats,
        'members': members,
        'lesson_completions': lesson_completions,
        'period': period
    }

    return render(request, 'departments/department_detail.html', context)