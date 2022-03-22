from django import forms
from django.db import models 
from django.core import validators
from django.contrib.auth.models import User

#login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


#class emailForm(forms.Form):
#    sender_name = forms.CharField()    
#    sender_email = forms.CharField(widget=forms.TextInput(attrs={'size': '30'}))
#    class Meta():
#        model = User
#        fields = ('first_name', 'last_name', 'username', 'email', 'password')
#        help_texts = {
#        'username': None