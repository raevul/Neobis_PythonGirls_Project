from django.forms import ModelForm
from django import forms

from .models import Girls


class GirlAddForm(ModelForm):
    class Meta:
        model = Girls
        fields = ['name', 'biography', 'image', 'category']
