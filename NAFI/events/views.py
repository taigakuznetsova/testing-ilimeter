from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    return render(request, 'events/event_detail.html', {'event': event})

@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})

@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})
