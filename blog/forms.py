from django.forms import ModelForm

from .models import Comment




class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["email", "comment"]
        exlcude = ["date"]
        labels = {
            "comment":"Leave a comment",
            "email":"Email Address"
        }