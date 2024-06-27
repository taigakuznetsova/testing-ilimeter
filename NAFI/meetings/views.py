from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Meeting
from .forms import MeetingForm
from notifications.models import Notification
from django.core.exceptions import PermissionDenied
from django.db import models
import requests

@login_required
def create_meeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST, user=request.user)
        if form.is_valid():
            response = requests.post(
                'https://api.daily.co/v1/rooms',
                headers={
                    'Authorization': f'Bearer {settings.DAILY_CO_API_KEY}',
                    'Content-Type': 'application/json'
                },
                json={
                    'properties': {
                        'enable_chat': True,
                        'enable_screenshare': True,
                        'start_video_off': True,
                        'start_audio_off': True,
                        'enable_people_ui': True,
                        'enable_prejoin_ui': True,
                        'enable_network_ui': True,
                        'enable_emoji_reactions': True,
                        'enable_hand_raising': True,
                        'enable_knocking': True
                    }
                }
            )
            data = response.json()
            meeting_url = data['url']

            meeting = form.save(commit=False)
            meeting.url = meeting_url
            meeting.host = request.user
            meeting.save()
            form.save_m2m()

            return redirect('meeting_detail', meeting_id=meeting.id)
    else:
        form = MeetingForm()
    return render(request, 'meetings/create_meeting.html', {'form': form})

@login_required
def meeting_detail(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    return render(request, 'meetings/meeting_detail.html', {'meeting': meeting})

@login_required
def edit_meeting(request, meeting_id):
    meeting = get_object_or_404(Meeting, id=meeting_id)
    if meeting.host != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = MeetingForm(request.POST, instance=meeting, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('meeting_detail', meeting_id=meeting.id)
    else:
        form = MeetingForm(instance=meeting, user=request.user)
    return render(request, 'meetings/edit_meeting.html', {'form': form, 'meeting': meeting})


@login_required
def user_meetings(request):
    sort_by = request.GET.get('sort_by', 'start_time')
    order = request.GET.get('order', 'asc')
    
    if order == 'desc':
        sort_by = '-' + sort_by
    
    meetings = Meeting.objects.filter(host=request.user).order_by(sort_by)
    return render(request, 'meetings/user_meetings.html', {'meetings': meetings, 'sort_by': sort_by, 'order': order})

@login_required
def calendar_view(request):
    meetings_host = Meeting.objects.filter(models.Q(host=request.user))
    meetings_participant = Meeting.objects.filter(models.Q(participants=request.user))
    return render(request, 'meetings/calendar.html', {'meetings_host': meetings_host, 'meetings_participant': meetings_participant})
