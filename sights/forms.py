from django import forms
from .models import Comment, ProposedLandmark, Landmark


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ProposedLandmarkForm(forms.ModelForm):
    class Meta:
        model = ProposedLandmark
        fields = ('name', 'information', 'type', 'address', 'path_photos', 'comment')

class FindForm(forms.Form):
    name = forms.CharField(required=False)
    information = forms.CharField(required=False)
    type = forms.CharField(required=False)
    address = forms.CharField(required=False)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
