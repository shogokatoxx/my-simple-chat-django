from django import forms
from .models import Post,Follow

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = ('follow',)
