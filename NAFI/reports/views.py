from django.shortcuts import render, redirect
from .forms import ReportForm

def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            # Сохраняем отчет
            report = form.save()
            # После успешного добавления отчета перенаправляем пользователя на главную страницу
            return redirect('home')
    else:
        form = ReportForm()
    return render(request, 'reports/create_report.html', {'form': form})
