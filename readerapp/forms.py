from django import forms
from django.contrib.auth.models import User
from writerapp.models import CommentModel



class AddCommentForm(forms.ModelForm):
    class Meta:
        model=CommentModel
        fields=['comment']
        widgets={
            
            "comment":forms.Textarea(attrs={"class":"form-control"}),
            
        }