from django import forms
from .models import Comment, Landmark, Photo


class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CommentForm(forms.Form):
    body = forms.CharField(label='',
                            widget=forms.Textarea)



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
    name = forms.CharField(label='Название')
    information = forms.CharField(label='Информация', widget=forms.Textarea)
    type = forms.CharField(label='Тип')
    address = forms.CharField(label='Адрес')
    comment = forms.CharField(label='Комментарий для администратора', widget=forms.Textarea)
    main_photo = forms.ImageField(required=False, label=u'Основное фото',
                              widget=forms.FileInput(attrs={'multiple': 'multiple'}))

    photos = forms.ImageField(required=False , label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))
