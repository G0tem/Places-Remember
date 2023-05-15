from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ['user', 'latitude', 'longitude', 'name', 'comment']