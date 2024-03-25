from django import forms
from .models import Comment


# Code Credit: I Think Therefore I Blog Walkthrough
class CommentForm(forms.ModelForm):
    """
    Form for users to comment on a post
    """
    class Meta:
        model = Comment
        fields = ('body',)
