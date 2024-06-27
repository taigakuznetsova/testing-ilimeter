from datetime import datetime
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import SignupView
from meetings.models import Meeting
from .forms import CustomSignupForm, CustomLoginForm, UserProfileForm
from courses.models import Module, UserProgress, UserCourse
from datetime import datetime, date
from .models import UserProfile

class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'account/register.html'

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'account/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

def get_greeting(request):
    current_time = datetime.now()
    current_hour = current_time.hour

    if 6 <= current_hour < 12:
        greeting = 'Доброе утро'
        emoji_path = '/static/img/sunrise.png'
    elif 12 <= current_hour < 18:
        greeting = 'Добрый день'
        emoji_path = '/static/img/sun.png'
    elif 18 <= current_hour < 24:
        greeting = 'Добрый вечер'
        emoji_path = '/static/img/sunset.png'
    else:
        greeting = 'Доброй ночи'
        emoji_path = '/static/img/moon.png'

    return f'{greeting}, {request.user.username} <img src="{emoji_path}" alt="emoji" class="emoji">'

@login_required
def profile(request):
    greeting = get_greeting(request=request)
    user = request.user
    
    user_courses = UserCourse.objects.filter(user=user)
    
    courses_progress = []
    
    for user_course in user_courses:
        course = user_course.course
        total_lessons = 0
        completed_lessons = 0
        
        modules = Module.objects.filter(course=course)
        for module in modules:
            module_total_lessons = module.lessons.count()
            module_completed_lessons = UserProgress.objects.filter(
                user=user, lesson__module=module, completed=True).count()
            
            total_lessons += module_total_lessons
            completed_lessons += module_completed_lessons
        
        if total_lessons > 0:
            progress_percent = int((completed_lessons / total_lessons) * 100)
        else:
            progress_percent = 0
        
        courses_progress.append({
            'course': course,
            'progress_percent': progress_percent
        })
    
    meetings_host = Meeting.objects.filter(host=user)
    meetings_participant = Meeting.objects.filter(participants=user)
    
    today = date.today()
    today_meetings = Meeting.objects.filter(
        start_time__date=today, 
        participants=user
    ).order_by('start_time')
    
    context = {
        'greeting': greeting,
        'courses_progress': courses_progress,
        'user': user,
        'meetings_host': meetings_host,
        'meetings_participant': meetings_participant,
        'today_meetings': today_meetings,
        'today': today.strftime("%B %d, %Y"),
        'today_weekday': today.strftime("%A")
    }
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'users/edit_profile.html', {'form': form})