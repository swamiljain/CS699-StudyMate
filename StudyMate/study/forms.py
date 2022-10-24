from dataclasses import field
import email
from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50,required=True,label="First Name",widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name=forms.CharField(max_length=50,required=True,label="Last Name")
    email=forms.EmailField(required=True, label="Email")

    class Meta:
        model=User
        fields=("first_name","last_name","username","email","password1","password2")

