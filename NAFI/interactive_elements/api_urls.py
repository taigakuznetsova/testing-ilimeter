from rest_framework.routers import DefaultRouter
from .api_views import (
    InteractiveViewSet, TextQuestionViewSet, TextAnswerViewSet,
    NumberQuestionViewSet, NumberAnswerViewSet, AudienceQAViewSet,
    NetworkingViewSet, StarVotingQuestionViewSet, StarVoteViewSet,
    SingleChoiceQuestionViewSet, SingleChoiceAnswerViewSet,
    MultipleChoiceQuestionViewSet, MultipleChoiceAnswerViewSet,
    SurveyViewSet, SurveyQuestionViewSet, SurveyAnswerViewSet,
    QuizViewSet, QuizAnswerViewSet
)

router = DefaultRouter()
router.register(r'interactives', InteractiveViewSet)
router.register(r'text-questions', TextQuestionViewSet)
router.register(r'text-answers', TextAnswerViewSet)
router.register(r'number-questions', NumberQuestionViewSet)
router.register(r'number-answers', NumberAnswerViewSet)
router.register(r'audience-qas', AudienceQAViewSet)
router.register(r'networkings', NetworkingViewSet)
router.register(r'star-voting-questions', StarVotingQuestionViewSet)
router.register(r'star-votes', StarVoteViewSet)
router.register(r'single-choice-questions', SingleChoiceQuestionViewSet)
router.register(r'single-choice-answers', SingleChoiceAnswerViewSet)
router.register(r'multiple-choice-questions', MultipleChoiceQuestionViewSet)
router.register(r'multiple-choice-answers', MultipleChoiceAnswerViewSet)
router.register(r'surveys', SurveyViewSet)
router.register(r'survey-questions', SurveyQuestionViewSet)
router.register(r'survey-answers', SurveyAnswerViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'quiz-answers', QuizAnswerViewSet)

urlpatterns = router.urls