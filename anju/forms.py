from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class AddForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','author','description','price','covers']


class RegestrtionForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class LoginForm(AuthenticationForm):
    pass