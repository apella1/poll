"""
Registering models to be modifiable via the admin panel
"""
from django.contrib import admin
from .models import Question, Choice

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    """Modifying the admin form to the desired fields

    Args:
        admin (_type_): _description_
    """

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]


# class ChoiceAdmin(admin.ModelAdmin):
#     fields = []


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
