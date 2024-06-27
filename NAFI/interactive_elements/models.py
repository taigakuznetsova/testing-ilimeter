import json
from django.db import models
from django.conf import settings
from meetings.models import Meeting


class Interactive(models.Model):
    INTERACTIVE_TYPES = [
        ('text_question', 'Открытый вопрос (текст)'),
        ('number_question', 'Открытый вопрос (число)'),
        ('audience_qa', 'Audience Q&A'),
        ('networking', 'Нетворкинг'),
        ('star_voting', 'Экспресс-голосование (звёздочки)'),
        ('single_choice', 'Экспресс-голосование (Single-choice)'),
        ('multiple_choice', 'Экспресс-голосование (Multiple choice)'),
        ('survey', 'Опрос по небольшой анкете'),
        ('quiz', 'Викторина'),
    ]
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name='interactives')
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=INTERACTIVE_TYPES)
    description = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    is_repeatable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Открытый вопрос (текст)
class TextQuestion(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='text_questions')
    question_text = models.TextField(blank=True, default='')
    max_length = models.PositiveIntegerField(default=1000)


class TextAnswer(models.Model):
    question = models.ForeignKey(TextQuestion, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Открытый вопрос (число)
class NumberQuestion(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='number_questions')
    question_text = models.TextField(blank=True, default='')
    min_value = models.FloatField(default=0)
    max_value = models.FloatField(default=100)


class NumberAnswer(models.Model):
    question = models.ForeignKey(NumberQuestion, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answer_number = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


# Audience Q&A
class AudienceQA(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='audience_qas')
    question_text = models.TextField(blank=True, default='')


# Нетворкинг
class Networking(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='networkings')
    description = models.TextField(blank=True, default='')
    session_duration = models.PositiveIntegerField(default=5)


# Экспресс-голосование (звёздочки)
class StarVotingQuestion(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='star_voting_questions')
    question_text = models.TextField(blank=True, default='')
    max_stars = models.PositiveIntegerField(default=5)


class StarVote(models.Model):
    question = models.ForeignKey(StarVotingQuestion, on_delete=models.CASCADE, related_name='votes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


# Экспресс-голосование (Single-choice)
class SingleChoiceQuestion(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='single_choice_questions')
    question_text = models.TextField(blank=True, default='')
    options = models.JSONField()


class SingleChoiceAnswer(models.Model):
    question = models.ForeignKey(SingleChoiceQuestion, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


# Экспресс-голосование (Multiple choice)
class MultipleChoiceQuestion(models.Model):
    interactive = models.ForeignKey(Interactive, on_delete=models.CASCADE, related_name='multiple_choice_questions')
    question_text = models.TextField(blank=True, default='')
    options = models.JSONField()
    max_choices = models.PositiveIntegerField(default=1)


class MultipleChoiceAnswer(models.Model):
    question = models.ForeignKey(MultipleChoiceQuestion, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    selected_options = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)


# Опрос по небольшой анкете
class Survey(models.Model):
    interactive = models.OneToOneField(Interactive, on_delete=models.CASCADE, related_name='survey')


class SurveyQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='survey_questions')
    question_text = models.TextField(blank=True, default='')


class SurveyAnswer(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# Викторина
class Quiz(models.Model):
    GAME_TYPE_CHOICES = [
        ('five_facts', '5 фактов'),
        ('thematic_quizzes', 'Тематические квизы'),
        ('association_game', 'Игра в ассоциации: три варианта'),
        ('unexpected_ending', 'История с неожиданным концом'),
    ]

    interactive = models.OneToOneField(Interactive, on_delete=models.CASCADE, related_name='quiz')
    game_type = models.CharField(max_length=100, choices=GAME_TYPE_CHOICES, default='five_facts')
    questions = models.JSONField()

    def get_questions_list(self):
        return json.loads(self.questions)


class QuizAnswer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answers = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)