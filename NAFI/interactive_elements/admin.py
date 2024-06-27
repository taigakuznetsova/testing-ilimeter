from django.contrib import admin
from .models import (Interactive, TextQuestion, NumberQuestion, StarVotingQuestion,
                     SingleChoiceQuestion, MultipleChoiceQuestion, Survey, SurveyQuestion, SurveyAnswer)


@admin.register(Interactive)
class InteractiveAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'meeting', 'is_active', 'is_repeatable', 'created_at')
    list_filter = ('type', 'is_active', 'is_repeatable', 'created_at')
    search_fields = ('title', 'description')


@admin.register(TextQuestion)
class TextQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'interactive')
    search_fields = ('question_text', 'interactive__title')


@admin.register(NumberQuestion)
class NumberQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'min_value', 'max_value', 'interactive')
    search_fields = ('question_text', 'interactive__title')


@admin.register(StarVotingQuestion)
class StarVotingQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'max_stars', 'interactive')
    search_fields = ('question_text', 'interactive__title')


@admin.register(SingleChoiceQuestion)
class SingleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'interactive', 'options')
    search_fields = ('question_text', 'interactive__title')


@admin.register(MultipleChoiceQuestion)
class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'interactive', 'options', 'max_choices')
    search_fields = ('question_text', 'interactive__title')


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('interactive', 'interactive_id')
    search_fields = ('interactive__title',)


@admin.register(SurveyQuestion)
class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'question_text')
    search_fields = ('question_text',)


@admin.register(SurveyAnswer)
class SurveyAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'answer_text', 'created_at')
    search_fields = ('question__question_text', 'user__username', 'answer_text')