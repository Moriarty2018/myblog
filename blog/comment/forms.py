from django import forms
from .models import Mycomment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Mycomment
        fields = ['name', 'email', 'url', 'text']
