from django import forms
from .models import Comment, ProposedLandmark


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ProposedLandmarkForm(forms.ModelForm):
    class Meta:
        model = ProposedLandmark
        fields = ('name', 'information', 'type', 'address', 'path_photos', 'comment')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
