from django import forms
from .models import (
    Interactive, TextQuestion, TextAnswer, NumberQuestion, NumberAnswer,
    AudienceQA, Networking, StarVotingQuestion, StarVote, SingleChoiceQuestion,
    SingleChoiceAnswer, MultipleChoiceQuestion, MultipleChoiceAnswer, Survey,
    SurveyQuestion, SurveyAnswer, Quiz, QuizAnswer
)
from meetings.models import Meeting


# Interactive Form
class InteractiveForm(forms.ModelForm):
    class Meta:
        model = Interactive
        fields = ['meeting', 'title', 'type', 'description', 'is_active', 'is_repeatable']

# Text Question Forms
class TextQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = TextQuestion
        fields = ['question_text', 'max_length', 'meeting', 'title', 'description']


class TextAnswerForm(forms.ModelForm):
    class Meta:
        model = TextAnswer
        fields = ['question', 'user', 'answer_text']

# Number Question Forms
class NumberQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = NumberQuestion
        fields = ['question_text', 'min_value', 'max_value', 'meeting', 'title', 'description']

class NumberAnswerForm(forms.ModelForm):
    class Meta:
        model = NumberAnswer
        fields = ['question', 'user', 'answer_number']

# Audience QA Form
class AudienceQAForm(forms.ModelForm):
    class Meta:
        model = AudienceQA
        fields = ['interactive', 'question_text']

# Networking Form
class NetworkingForm(forms.ModelForm):
    class Meta:
        model = Networking
        fields = ['interactive', 'description', 'session_duration']

# Star Voting Forms
class StarVotingQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = StarVotingQuestion
        fields = ['question_text', 'max_stars', 'meeting', 'title', 'description']


class StarVoteForm(forms.ModelForm):
    class Meta:
        model = StarVote
        fields = ['question', 'user', 'stars']

# Single Choice Forms
class SingleChoiceQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = SingleChoiceQuestion
        fields = ['question_text', 'meeting', 'title', 'description']

class SingleChoiceAnswerForm(forms.ModelForm):
    class Meta:
        model = SingleChoiceAnswer
        fields = ['question', 'user', 'selected_option']

# Multiple Choice Forms
class MultipleChoiceQuestionForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)
    max_choices = forms.IntegerField(min_value=1, required=True, label='Максимальное количество вариантов')

    class Meta:
        model = MultipleChoiceQuestion
        fields = ['question_text', 'meeting', 'title', 'description', 'max_choices']

class MultipleChoiceAnswerForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceAnswer
        fields = ['question', 'user', 'selected_options']

# Survey Forms
class SurveyForm(forms.ModelForm):
    meeting = forms.ModelChoiceField(queryset=Meeting.objects.all(), required=True)
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Survey
        fields = ['meeting', 'title', 'description']

class SurveyQuestionForm(forms.ModelForm):
    class Meta:
        model = SurveyQuestion
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 1}),
        }

class SurveyAnswerForm(forms.ModelForm):
    class Meta:
        model = SurveyAnswer
        fields = ['question', 'user', 'answer_text']

# Quiz Forms
class QuizForm(forms.ModelForm):
    game_type = forms.ChoiceField(choices=Quiz.GAME_TYPE_CHOICES, required=True)
    questions = forms.JSONField()

    class Meta:
        model = Quiz
        fields = ['game_type', 'questions']

class QuizAnswerForm(forms.ModelForm):
    class Meta:
        model = QuizAnswer
        fields = ['quiz', 'user', 'answers']