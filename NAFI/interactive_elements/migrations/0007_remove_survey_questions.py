# Generated by Django 5.0.6 on 2024-06-22 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactive_elements', '0006_alter_interactive_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='questions',
        ),
    ]