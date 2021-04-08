from rest_framework import serializers

from .models import Quiz, Question, Participant

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    quiz =serializers.IntegerField(source="quiz_id")
    variants = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Question
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        exclude = ('point',)

class ParticipanFinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'