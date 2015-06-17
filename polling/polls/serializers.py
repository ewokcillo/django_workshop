# coding=utf-8
from rest_framework import serializers
from polls.models import Questionary, Question, Choice, Answer


class QuestionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionary


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
