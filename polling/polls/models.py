from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Questionary(models.Model):
    name = models.CharField(max_length=200)


class Question(models.Model):
    questionary = models.ForeignKey(Questionary)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Answer(models.Model):
    user = models.ForeignKey(User)
    Choice = models.ForeignKey(Choice)
