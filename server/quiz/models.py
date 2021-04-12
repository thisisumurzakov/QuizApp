from django.db import models
from django.contrib.postgres.fields import ArrayField


class Quiz(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, related_name='questions')
    question = models.CharField(max_length=250)
    variants = ArrayField(models.CharField(max_length=250))
    correct_variant_index = models.PositiveSmallIntegerField()

class Participant(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='participant', null=True, blank=True)
    point = models.PositiveSmallIntegerField(blank=True, null=True)
