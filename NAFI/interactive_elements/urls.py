from django.urls import path
from .views import (
    InteractiveListView,
    TextQuestionCreateView, TextQuestionUpdateView, TextQuestionDetailView, TextAnswerCreateView,
    NumberQuestionCreateView, NumberQuestionUpdateView, NumberQuestionDetailView, NumberAnswerCreateView,
    AudienceQACreateView,
    NetworkingCreateView,
    StarVotingQuestionCreateView, StarVotingQuestionUpdateView, StarVotingQuestionDetailView, StarVoteCreateView,
    SingleChoiceQuestionCreateView, SingleChoiceQuestionUpdateView, SingleChoiceQuestionDetailView, SingleChoiceAnswerCreateView,
    MultipleChoiceQuestionCreateView, MultipleChoiceQuestionUpdateView, MultipleChoiceQuestionDetailView, MultipleChoiceAnswerCreateView,
    SurveyCreateAndAddQuestionView, SurveyQuestionUpdateView, SurveyQuestionDetailView, SurveyAnswerCreateView,
    QuizCreateView, QuizUpdateView, QuizDetailView, QuizAnswerCreateView
)

urlpatterns = [
    # Interactive URLs
    path('interactives/', InteractiveListView.as_view(), name='interactive_list'),

    # Text Question URLs
    path('interactives/text-question/create/', TextQuestionCreateView.as_view(), name='text_question_create'),
    # path('interactives/text-question/<int:pk>/update/', TextQuestionUpdateView.as_view(), name='text_question_update'),
    # path('interactives/text-answer/<int:pk>/', TextQuestionDetailView.as_view(), name='text_answer_detail'),
    # path('interactives/text-answer/create/', TextAnswerCreateView.as_view(), name='text_answer_create'),

    # Number Question URLs
    path('interactives/number-question/create/', NumberQuestionCreateView.as_view(), name='number_question_create'),
    # path('interactives/number-question/<int:pk>/update/', NumberQuestionUpdateView.as_view(), name='number_question_update'),
    # path('interactives/number-answer/<int:pk>/', NumberQuestionDetailView.as_view(), name='number_answer_detail'),
    # path('interactives/number-answer/create/', NumberAnswerCreateView.as_view(), name='number_answer_create'),

    # Audience QA URLs
    path('audience-qa/create/', AudienceQACreateView.as_view(), name='audience_qa_create'),

    # Networking URLs
    path('networking/create/', NetworkingCreateView.as_view(), name='networking_create'),

    # Star Voting URLs
    path('interactives/star-voting-question/create/', StarVotingQuestionCreateView.as_view(), name='star_voting_question_create'),
    # path('interactives/star-voting-question/<int:pk>/update/', StarVotingQuestionUpdateView.as_view(), name='star_voting_question_update'),
    # path('interactives/star-voting-question/<int:pk>/', StarVotingQuestionDetailView.as_view(), name='star_voting_question_detail'),
    # path('interactives/star-vote/create/', StarVoteCreateView.as_view(), name='star_vote_create'),

    # Single Choice URLs
    path('interactives/single-choice-question/create/', SingleChoiceQuestionCreateView.as_view(), name='single_choice_question_create'),
    # path('interactives/single-choice-question/<int:pk>/update/', SingleChoiceQuestionUpdateView.as_view(), name='single_choice_question_update'),
    # path('interactives/single-choice-question/<int:pk>/', SingleChoiceQuestionDetailView.as_view(), name='single_choice_question_detail'),
    # path('interactives/single-choice-answer/create/', SingleChoiceAnswerCreateView.as_view(), name='single_choice_answer_create'),

    # Multiple Choice URLs
    path('interactives/multiple-choice-question/create/', MultipleChoiceQuestionCreateView.as_view(), name='multiple_choice_question_create'),
    # path('interactives/multiple-choice-question/<int:pk>/update/', MultipleChoiceQuestionUpdateView.as_view(), name='multiple_choice_question_update'),
    # path('interactives/multiple-choice-question/<int:pk>/', MultipleChoiceQuestionDetailView.as_view(), name='multiple_choice_question_detail'),
    # path('interactives/multiple-choice-answer/create/', MultipleChoiceAnswerCreateView.as_view(), name='multiple_choice_answer_create'),

    # Survey URLs
    path('interactives/survey-question/create/', SurveyCreateAndAddQuestionView.as_view(), name='survey_create'),
    # path('interactives/survey-question/<int:pk>/update/', SurveyQuestionUpdateView.as_view(), name='survey_question_update'),
    # path('interactives/survey-question/<int:pk>/', SurveyQuestionDetailView.as_view(), name='survey_question_detail'),
    # path('interactives/survey-answer/create/', SurveyAnswerCreateView.as_view(), name='survey_answer_create'),

    # Quiz URLs
    path('interactives/quiz/create/', QuizCreateView.as_view(), name='quiz_create'),
    # path('interactives/quiz/<int:pk>/update/', QuizUpdateView.as_view(), name='quiz_update'),
    # path('interactives/quiz/<int:pk>/', QuizDetailView.as_view(), name='quiz_detail'),
    # path('interactives/quiz-answer/create/', QuizAnswerCreateView.as_view(), name='quiz_answer_create'),
]