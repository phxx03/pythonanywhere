from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Novels
from django.forms import ModelForm

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class Novely(ModelForm):
    class Meta:
        model = Novels
        fields = ['TypeName','Fimg','FictionName','FWriterName','Material']


searchchoices = (
        ('Y' , 'Y'),
        ('Drama' , 'Drama'),
        ('Action' , 'Action'),
        ('Fantasy' , 'Fantasy'),
    )

class SearchForm(forms.Form):
    SearchBy = forms.ChoiceField(choices=searchchoices)