from django import forms
from .models import Comment, Landmark, Photo


class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CommentForm(forms.Form):
    body = forms.CharField(label='',
                            widget=forms.Textarea)



class FindForm(forms.Form):
    name = forms.CharField(required=False, label='Название')
    information = forms.CharField(required=False, label='Информация')
    type = forms.CharField(required=False, label='Тип')
    address = forms.CharField(required=False, label='Адрес')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProposedLandmarkForm(forms.Form):
    name = forms.CharField(label='Название')
    information = forms.CharField(label='Информация', widget=forms.Textarea)
    type = forms.CharField(label='Тип')
    address = forms.CharField(label='Адрес')
    comment = forms.CharField(label='Комментарий для администратора'    , widget=forms.Textarea)
    main_photo = forms.ImageField(required=False, label=u'Основное фото',
                              widget=forms.FileInput(attrs={'multiple': 'multiple'}))

    photos = forms.ImageField(required=False , label=u'Ещё фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))
