from django import forms
from django.contrib.auth import get_user_model
from .models import Meeting
from django.core.exceptions import ValidationError
from django.utils import timezone

User = get_user_model()

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class MeetingForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    start_time = forms.DateTimeField(widget=DateTimeInput(attrs={'min': timezone.now().isoformat()}))
    end_time = forms.DateTimeField(widget=DateTimeInput(attrs={'min': timezone.now().isoformat()}))

    class Meta:
        model = Meeting
        fields = ['title', 'description', 'start_time', 'end_time', 'participants']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MeetingForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['participants'].queryset = User.objects.exclude(id=user.id)
            
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            if start_time < timezone.now():
                self.add_error('start_time', "The start time cannot be in the past.")
            if end_time <= start_time:
                self.add_error('end_time', "The end time cannot be earlier (or equal) than the start time.")

        return cleaned_data
