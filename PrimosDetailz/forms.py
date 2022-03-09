from django import forms
#from django.db import models 
from django.core import validators
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
