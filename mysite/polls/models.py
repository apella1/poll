"""
Polls models
"""
import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Question model

    Args:
        models (_type_): _description_
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # It’s important to add __str__() methods to your models,
    # not only for your own convenience
    # when dealing with the interactive prompt,
    # but also because objects’ representations are used
    # throughout Django’s automatically-generated admin.
    def __str__(self):
        return str(self.question_text)

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?"
        )
    def was_published_recently(self):
        """returns True if a question was published within the last one day

        Returns:
            _type_: _description_
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """Choice model

    Args:
        models (_type_): _description_
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.choice_text)
