from django.core.management.base import BaseCommand
from django.utils import timezone
from courses.models import Course, Module, Lesson

class Command(BaseCommand):
    help = 'Creates example courses with modules and lessons'

    def handle(self, *args, **kwargs):
        course1 = Course.objects.create(
            title='Основы информационных технологий',
            description='Курс по основам информационных технологий для начинающих.',
            price=0.00,
            is_free=True,
            created_at=timezone.now()
        )

        for i in range(1, 4):
            module = Module.objects.create(
                course=course1,
                title=f'Модуль {i}',
                description=f'Описание модуля {i}',
                order=i,
                created_at=timezone.now()
            )

            for j in range(1, 3):
                Lesson.objects.create(
                    module=module,
                    title=f'Урок {j} в модуле {i}',
                    content=f'Содержание урока {j} в модуле {i}',
                    order=j,
                    created_at=timezone.now()
                )

        course2 = Course.objects.create(
            title='Основы маркетинга',
            description='Курс по основам маркетинга для малого бизнеса.',
            price=0.00,
            is_free=True,
            created_at=timezone.now()
        )

        for i in range(1, 4):
            module = Module.objects.create(
                course=course2,
                title=f'Модуль {i}',
                description=f'Описание модуля {i}',
                order=i,
                created_at=timezone.now()
            )

            for j in range(1, 3):
                Lesson.objects.create(
                    module=module,
                    title=f'Урок {j} в модуле {i}',
                    content=f'Содержание урока {j} в модуле {i}',
                    order=j,
                    created_at=timezone.now()
                )

        self.stdout.write(self.style.SUCCESS('Курсы и их содержимое успешно созданы!'))
