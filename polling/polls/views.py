from rest_framework import viewsets

from polls.models import Questionary, Question, Choice, Answer
from polls.serializers import (QuestionarySerializer, QuestionSerializer,
                               ChoiceSerializer, AnswerSerializer)


class QuestionaryViewSet(viewsets.ModelViewSet):
    queryset = Questionary.objects.all()
    serializer_class = QuestionarySerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
