from django import forms
from django.core import validators

class ContactForm(forms.Form):
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
