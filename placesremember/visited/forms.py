from django import forms
from django.template.context_processors import request

from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ['user', 'latitude', 'longitude', 'name', 'comment']

        widgets = {
            'user': forms.TextInput(attrs={'style': 'display:none'}),
            'comment': forms.Textarea(attrs={'cols': 20, 'rows': 10}),
        }