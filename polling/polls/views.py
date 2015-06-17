from rest_framework import viewsets

from polls.models import Questionary
from polls.serializers import QuestionarySerializer


class QuestionaryViewSet(viewsets.ModelViewSet):
    queryset = Questionary.objects.all()
    serializer_class = QuestionarySerializer

