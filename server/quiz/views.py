from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import QuizSerializer, QuestionSerializer, ParticipantSerializer, ParticipanFinishSerializer
from .models import Quiz, Question, Participant

class QuizPostView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionPostView(APIView):
    def post(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)
        for i in range(0, len(request.data['data'])):
            request.data['data'][i]["quiz"] = quiz.id
        serializer = QuestionSerializer(data=request.data['data'], many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data=request.data)

class GetQuestionView(APIView):
    def get(self, request, pk1, pk2):
        quiz = get_object_or_404(Quiz, pk=pk1)
        question = get_object_or_404(Question, pk=pk2)
        if quiz == question.quiz:
            serializer = QuestionSerializer(question).data
            serializer.pop("correct_variant_index")
            return Response(status=201, data=serializer)

class FinishQuizView(APIView):
    def post(self, request, pk):
        quiz = get_object_or_404(Quiz, pk=pk)
        quiz_questions = quiz.questions.all()
        ids = []
        correct = 0
        for question in quiz_questions:
            ids.append(question.id)
        for data in request.data["data"]:
            if data["question_id"] in ids and data['correct_variant_index']==quiz.questions.get(pk=data["question_id"]).correct_variant_index:
                correct+=1
        participant = get_object_or_404(Participant, pk=request.data["participant_id"])
        participant.point = correct
        return Response(status=201, data=ParticipanFinishSerializer(participant).data)

class StartQuizView(APIView):
    def post(self, request, pk):
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["quiz"] = get_object_or_404(Quiz, pk=pk)
            serializer.save()
            return Response(status=201, data=serializer.data)
        return Response(status=400)
