from django import forms
from .models import Comment, Landmark, Photo


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

#class ProposedLandmarkForm(forms.ModelForm):
#    class Meta:
#        model = ProposedLandmark
#        fields = ('name', 'information', 'type', 'address', 'path_photos', 'comment')

class FindForm(forms.Form):
    name = forms.CharField(required=False)
    information = forms.CharField(required=False)
    type = forms.CharField(required=False)
    address = forms.CharField(required=False)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProposedLandmarkForm(forms.Form):
    name = forms.CharField()
    information = forms.CharField()
    type = forms.CharField()
    address = forms.CharField()
    comment = forms.CharField()
    photos = forms.ImageField(required=False , label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))
