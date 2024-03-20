from .models import Comment
from django import forms

# Code Credit: I Think Therefore I Blog Walkthrough
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)