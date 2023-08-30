"""
Registering models to be modifiable via the admin panel
"""
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
