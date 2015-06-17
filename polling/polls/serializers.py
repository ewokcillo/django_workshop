# coding=utf-8
from rest_framework import serializers
from polls.models import Questionary


class QuestionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionary
