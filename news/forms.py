from django.forms import models
from .models import Girls


class GirlAddForm(models.ModelForm):
    class Meta:
        model = Girls
        fields = ['name', 'biography', 'image', 'category']
