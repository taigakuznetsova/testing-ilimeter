from rest_framework import serializers
from .models import (
    Interactive, TextQuestion, TextAnswer, NumberQuestion, NumberAnswer,
    AudienceQA, Networking, StarVotingQuestion, StarVote, SingleChoiceQuestion,
    SingleChoiceAnswer, MultipleChoiceQuestion, MultipleChoiceAnswer, Survey,
    SurveyQuestion, SurveyAnswer, Quiz, QuizAnswer
)

class InteractiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interactive
        fields = '__all__'

class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQuestion
        fields = '__all__'

class TextAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextAnswer
        fields = '__all__'

class NumberQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberQuestion
        fields = '__all__'

class NumberAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberAnswer
        fields = '__all__'

class AudienceQASerializer(serializers.ModelSerializer):
    class Meta:
        model = AudienceQA
        fields = '__all__'

class NetworkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Networking
        fields = '__all__'

class StarVotingQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarVotingQuestion
        fields = '__all__'

class StarVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarVote
        fields = '__all__'

class SingleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleChoiceQuestion
        fields = '__all__'

class SingleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleChoiceAnswer
        fields = '__all__'

class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceQuestion
        fields = '__all__'

class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceAnswer
        fields = '__all__'

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'

class SurveyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyQuestion
        fields = '__all__'

class SurveyAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyAnswer
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswer
        fields = '__all__'