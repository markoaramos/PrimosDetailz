from django import forms
from django.db import models 
from django.core import validators
from django.contrib.auth.models import User

#login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())