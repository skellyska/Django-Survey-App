"""
created two models: Question and Choice. A Question has a question and a publication date
A Choice has two fields: the text of the choice and a vote tally
Each Choice is associated with a Question


"""

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)