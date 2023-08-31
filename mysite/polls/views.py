"""
Views for the polls app
"""

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# from django.http import Http404
# from django.template import loader
from .models import Question


def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # using loader
    # template = loader.get_template("polls/index.html")
    # context variable remains
    context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """_summary_

    Args:
        request (_type_): _description_
        question_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # using a shortcut for the above code
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    """_summary_

    Args:
        request (_type_): _description_
        question_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """_summary_

    Args:
        request (_type_): _description_
        question_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    return HttpResponse("You're voting on question %s." % question_id)
