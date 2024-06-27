from django.db import models
from django.conf import settings
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from notifications.models import Notification


User = get_user_model()


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField()
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='meetings_participants')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        participant_group, created = Group.objects.get_or_create(name='Participant')
        for participant in self.participants.all():
            participant.groups.add(participant_group)
            
    def __str__(self):
        return self.title

@receiver(m2m_changed, sender=Meeting.participants.through)
def participants_changed(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            Notification.objects.create(
                user=user,
                message=f'You have been added to the meeting "{instance.title}" by {instance.host.username}.',
                link=instance.url
            )
            
    elif action == "post_remove":
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            Notification.objects.create(
                user=user,
                message=f'You have been removed from the meeting "{instance.title}" by {instance.host.username}.'
            )
