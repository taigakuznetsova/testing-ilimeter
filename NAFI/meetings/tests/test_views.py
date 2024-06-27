from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from meetings.models import Meeting

User = get_user_model()

class MeetingViewsTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.host_user = User.objects.create_user(username='hostuser', password='password123')
        self.participant_user = User.objects.create_user(username='participantuser', password='password123')
        self.meeting = Meeting.objects.create(
            title='Test Meeting',
            description='This is a test meeting',
            url='https://example.com/meeting',
            host=self.host_user,
        )
        self.meeting.participants.add(self.participant_user)
    
    def test_meeting_detail_view(self):
        self.client.login(username='participantuser', password='password123')
        response = self.client.get(reverse('meeting_detail', args=[self.meeting.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Meeting')
        self.assertContains(response, 'This is a test meeting')
    
    def test_create_meeting_view(self):
        self.client.login(username='hostuser', password='password123')
        response = self.client.post(reverse('create_meeting'), {
            'title': 'New Meeting',
            'description': 'This is a new meeting',
            'url': 'https://example.com/new-meeting/',
            'start_time': '2024-06-25 10:00:00',
            'participants': [self.participant_user.pk],
        })
        self.assertEqual(response.status_code, 302)  # Redirects to meeting detail page
    
    def test_edit_meeting_view(self):
        self.client.login(username='hostuser', password='password123')
        response = self.client.post(reverse('edit_meeting', args=[self.meeting.pk]), {
            'title': 'Updated Meeting',
            'description': 'This is an updated meeting',
            'url': 'https://example.com/updated-meeting/',
            'start_time': '2024-06-25 10:00:00',
            'participants': [self.participant_user.pk],
        })
        self.assertEqual(response.status_code, 302)
