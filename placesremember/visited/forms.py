from django import forms

from .models import Places


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ['user', 'latitude', 'longitude', 'name', 'comment']

        widgets = {
            'user': forms.TextInput(attrs={'style': 'display:none'}),
            'comment': forms.Textarea(attrs={'cols': 20, 'rows': 10}),
        }
