from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from meetings.models import Meeting
from notifications.models import Notification

User = get_user_model()

class MeetingModelTestCase(TestCase):
    
    def setUp(self):
        self.host_user = User.objects.create_user(username='hostuser', password='password123')
        self.participant_user = User.objects.create_user(username='participantuser', password='password123')
        self.meeting = Meeting.objects.create(
            title='Test Meeting',
            description='This is a test meeting',
            url='https://example.com/meeting',
            host=self.host_user,
            start_time=timezone.now(),
        )
        self.meeting.participants.add(self.participant_user)
    
    def test_meeting_creation(self):
        self.assertEqual(self.meeting.title, 'Test Meeting')
        self.assertEqual(self.meeting.description, 'This is a test meeting')
        self.assertEqual(self.meeting.url, 'https://example.com/meeting')
        self.assertEqual(self.meeting.host, self.host_user)
        self.assertIn(self.participant_user, self.meeting.participants.all())
    
    def test_notification_creation_on_participant_add(self):
        initial_count = Notification.objects.count()
        self.meeting.participants.add(User.objects.create_user(username='newparticipant', password='password123'))
        self.assertEqual(Notification.objects.count(), initial_count + 1)
    
    def test_notification_creation_on_participant_remove(self):
        initial_count = Notification.objects.count()
        self.meeting.participants.remove(self.participant_user)
        self.assertEqual(Notification.objects.count(), initial_count + 1)
