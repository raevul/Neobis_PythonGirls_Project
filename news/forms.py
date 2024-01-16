from django.forms import ModelForm

from .models import News


class NewCreateForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'image']
