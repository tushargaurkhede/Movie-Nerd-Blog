from django import forms
from .models import BlogPost, Comment
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('commenter', 'comment',)
