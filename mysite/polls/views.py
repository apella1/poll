"""
Views for the polls app
"""

from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    """_summary_

    Args:
        request (_type_): _description_
        question_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    return HttpResponse("You're looking at question %s." % question_id)


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
