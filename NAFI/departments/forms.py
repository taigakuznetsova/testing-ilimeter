from django import forms
from django.contrib.auth.models import User
from .models import Department
from courses.models import Course
from django.contrib.auth import get_user_model


User = get_user_model()

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'head']

class AddMemberForm(forms.ModelForm):
    new_members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Department
        fields = []

class AddCourseForm(forms.ModelForm):
    new_courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Department
        fields = []
        