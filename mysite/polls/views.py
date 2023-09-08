"""
Views for the polls app
"""
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

# from django.http import Http404
# from django.template import loader
from .models import Choice, Question


class IndexView(generic.ListView):
    """Index view

    Args:
        generic (_type_): _description_

    Returns:
        _type_: _description_
    """

    template_name: str = "polls/index.html"
    context_object_name: str = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions.
        Not including those set to be published in the future.
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    """Detail view

    Args:
        generic (_type_): _description_
    """

    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes all unpublished questions
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    """_summary_

    Args:
        generic (_type_): _description_
    """

    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    """Voting on a particular question and selecting the available options

    Args:
        request (_type_): _description_
        question_id (int): id of the current question

    Returns:
        _type_: _description_
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Re-displaying question form
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You did not select a choice"
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice
        # should a user press the back button
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,))
            )
