from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from meetings.models import Meeting
from interactive_elements.models import TextQuestion, NumberQuestion, AudienceQA, Networking, StarVoting, SingleChoice, MultipleChoice, Survey, Quiz
from departments.models import Department
from courses.models import UserCourse


class Command(BaseCommand):
    help = 'Create initial groups and permissions'

    def handle(self, *args, **options):
        admin_group, created = Group.objects.get_or_create(name='Admin')
        organizer_group, created = Group.objects.get_or_create(name='Organizer')
        participant_group, created = Group.objects.get_or_create(name='Participant')
        user_group, created = Group.objects.get_or_create(name='User')
        guest_group, created = Group.objects.get_or_create(name='Guest')
        moderator_group, created = Group.objects.get_or_create(name='Moderator')
        analyst_group, created = Group.objects.get_or_create(name='Analyst')
        leader_group, created = Group.objects.get_or_create(name='Leader')

        meeting_ct = ContentType.objects.get_for_model(Meeting)
        interactive_cts = [
            ContentType.objects.get_for_model(TextQuestion),
            ContentType.objects.get_for_model(NumberQuestion),
            ContentType.objects.get_for_model(AudienceQA),
            ContentType.objects.get_for_model(Networking),
            ContentType.objects.get_for_model(StarVoting),
            ContentType.objects.get_for_model(SingleChoice),
            ContentType.objects.get_for_model(MultipleChoice),
            ContentType.objects.get_for_model(Survey),
            ContentType.objects.get_for_model(Quiz),
        ]

        department_ct = ContentType.objects.get_for_model(Department)
        user_course_ct = ContentType.objects.get_for_model(UserCourse)

        perms = {
            'can_create_meeting': Permission.objects.get_or_create(codename='can_create_meeting',
                                                                   name='Can create meeting',
                                                                   content_type=meeting_ct)[0],
            'can_edit_meeting': Permission.objects.get_or_create(codename='can_edit_meeting',
                                                                 name='Can edit meeting',
                                                                 content_type=meeting_ct)[0],
            'can_delete_meeting': Permission.objects.get_or_create(codename='can_delete_meeting',
                                                                   name='Can delete meeting',
                                                                   content_type=meeting_ct)[0],
            'can_view_meeting': Permission.objects.get_or_create(codename='can_view_meeting',
                                                                 name='Can view meeting',
                                                                 content_type=meeting_ct)[0],
            'can_manage_users': Permission.objects.get_or_create(codename='can_manage_users',
                                                                 name='Can manage users',
                                                                 content_type=meeting_ct)[0],
            'can_view_analytics': Permission.objects.get_or_create(codename='can_view_analytics',
                                                                   name='Can view analytics',
                                                                   content_type=meeting_ct)[0],
            'can_manage_department': Permission.objects.get_or_create(codename='can_manage_department',
                                                                       name='Can manage department',
                                                                       content_type=department_ct)[0],
            'can_view_department_courses': Permission.objects.get_or_create(codename='can_view_department_courses',
                                                                            name='Can view department courses',
                                                                            content_type=user_course_ct)[0],
        }

        interactive_perms = {
            'can_create_interactive': Permission.objects.get_or_create(codename='can_create_interactive',
                                                                       name='Can create interactive',
                                                                       content_type=interactive_cts[0])[0],
            'can_edit_interactive': Permission.objects.get_or_create(codename='can_edit_interactive',
                                                                     name='Can edit interactive',
                                                                     content_type=interactive_cts[0])[0],
            'can_delete_interactive': Permission.objects.get_or_create(codename='can_delete_interactive',
                                                                       name='Can delete interactive',
                                                                       content_type=interactive_cts[0])[0],
            'can_view_interactive': Permission.objects.get_or_create(codename='can_view_interactive',
                                                                     name='Can view interactive',
                                                                     content_type=interactive_cts[0])[0],
        }

        admin_group.permissions.set(list(perms.values()) + list(interactive_perms.values()))
        organizer_group.permissions.set([
            perms['can_create_meeting'],
            perms['can_edit_meeting'],
            perms['can_view_meeting'],
            interactive_perms['can_create_interactive'],
            interactive_perms['can_edit_interactive'],
            interactive_perms['can_view_interactive'],
        ])
        participant_group.permissions.set([
            perms['can_view_meeting'],
            interactive_perms['can_view_interactive'],
        ])
        moderator_group.permissions.set([
            perms['can_edit_meeting'],
            perms['can_delete_meeting'],
            perms['can_view_meeting'],
            perms['can_manage_users'],
            interactive_perms['can_edit_interactive'],
            interactive_perms['can_delete_interactive'],
            interactive_perms['can_view_interactive'],
        ])
        analyst_group.permissions.set([
            perms['can_view_analytics'],
        ])
        leader_group.permissions.set([
            perms['can_manage_department'],
            perms['can_view_department_courses'],
        ])

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully'))
