"""
Registering models to be modifiable via the admin panel
"""
from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    """_summary_

    Args:
        admin (_type_): _description_
    """

    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """Modifying the admin form to the desired fields

    Args:
        admin (_type_): _description_
    """

    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]

    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


# class ChoiceAdmin(admin.ModelAdmin):
#     fields = []


admin.site.register(Question, QuestionAdmin)
