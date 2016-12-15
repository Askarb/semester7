from django.db import models


class Question(models.Model):
    question = models.TextField()


class Answer(models.Model):
    book_id = models.PositiveIntegerField()
    answer = models.TextField()

