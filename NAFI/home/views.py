from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/home_authenticated.html')
    else:
        return render(request, 'home/home_unauthenticated.html')
    
@login_required
def dashboard(request):
    context = {
        'user': request.user,
    }
    return render(request, 'home/dashboard.html', context)