from rest_framework import viewsets
from .models import (
    Interactive, TextQuestion, TextAnswer, NumberQuestion, NumberAnswer,
    AudienceQA, Networking, StarVotingQuestion, StarVote, SingleChoiceQuestion,
    SingleChoiceAnswer, MultipleChoiceQuestion, MultipleChoiceAnswer, Survey,
    SurveyQuestion, SurveyAnswer, Quiz, QuizAnswer
)
from .serializers import (
    InteractiveSerializer, TextQuestionSerializer, TextAnswerSerializer,
    NumberQuestionSerializer, NumberAnswerSerializer, AudienceQASerializer,
    NetworkingSerializer, StarVotingQuestionSerializer, StarVoteSerializer,
    SingleChoiceQuestionSerializer, SingleChoiceAnswerSerializer,
    MultipleChoiceQuestionSerializer, MultipleChoiceAnswerSerializer,
    SurveySerializer, SurveyQuestionSerializer, SurveyAnswerSerializer,
    QuizSerializer, QuizAnswerSerializer
)

class InteractiveViewSet(viewsets.ModelViewSet):
    queryset = Interactive.objects.all()
    serializer_class = InteractiveSerializer

class TextQuestionViewSet(viewsets.ModelViewSet):
    queryset = TextQuestion.objects.all()
    serializer_class = TextQuestionSerializer

class TextAnswerViewSet(viewsets.ModelViewSet):
    queryset = TextAnswer.objects.all()
    serializer_class = TextAnswerSerializer

class NumberQuestionViewSet(viewsets.ModelViewSet):
    queryset = NumberQuestion.objects.all()
    serializer_class = NumberQuestionSerializer

class NumberAnswerViewSet(viewsets.ModelViewSet):
    queryset = NumberAnswer.objects.all()
    serializer_class = NumberAnswerSerializer

class AudienceQAViewSet(viewsets.ModelViewSet):
    queryset = AudienceQA.objects.all()
    serializer_class = AudienceQASerializer

class NetworkingViewSet(viewsets.ModelViewSet):
    queryset = Networking.objects.all()
    serializer_class = NetworkingSerializer

class StarVotingQuestionViewSet(viewsets.ModelViewSet):
    queryset = StarVotingQuestion.objects.all()
    serializer_class = StarVotingQuestionSerializer

class StarVoteViewSet(viewsets.ModelViewSet):
    queryset = StarVote.objects.all()
    serializer_class = StarVoteSerializer

class SingleChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = SingleChoiceQuestion.objects.all()
    serializer_class = SingleChoiceQuestionSerializer

class SingleChoiceAnswerViewSet(viewsets.ModelViewSet):
    queryset = SingleChoiceAnswer.objects.all()
    serializer_class = SingleChoiceAnswerSerializer

class MultipleChoiceQuestionViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoiceQuestion.objects.all()
    serializer_class = MultipleChoiceQuestionSerializer

class MultipleChoiceAnswerViewSet(viewsets.ModelViewSet):
    queryset = MultipleChoiceAnswer.objects.all()
    serializer_class = MultipleChoiceAnswerSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyQuestionViewSet(viewsets.ModelViewSet):
    queryset = SurveyQuestion.objects.all()
    serializer_class = SurveyQuestionSerializer

class SurveyAnswerViewSet(viewsets.ModelViewSet):
    queryset = SurveyAnswer.objects.all()
    serializer_class = SurveyAnswerSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizAnswerViewSet(viewsets.ModelViewSet):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerSerializer