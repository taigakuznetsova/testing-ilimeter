from rest_framework import serializers
from .models import Department
from courses.models import Course
from django.contrib.auth import get_user_model

User = get_user_model()

class DepartmentSerializer(serializers.ModelSerializer):
    head = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    members = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())

    class Meta:
        model = Department
        fields = '__all__'