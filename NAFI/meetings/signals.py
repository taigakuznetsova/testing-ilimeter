from django.contrib.auth.models import Group
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:
        user_group, created = Group.objects.get_or_create(name='User')
        participant_group, created = Group.objects.get_or_create(name='Participant')
        instance.groups.add(user_group)
        instance.groups.add(participant_group)
