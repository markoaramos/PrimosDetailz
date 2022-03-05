import email
from email import message
from http import client
import re
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method =='POST':      
        sender_name = request.POST['name']
        sender_email = request.POST['email']
        message = request.POST['message']
        sender_data = {
            'sender_name': sender_name,
            'sender_email': sender_email,
            'subject': 'Primos Detailz New Message from ' + sender_name,
            'message': message
        }
        print(sender_data)

        send_mail(
            'Message From: '+ sender_email, #subject
            message, #message
            sender_email, #from email,
            ['primosdetailz@gmail.com'], #to Email
        )
        return render(request, 'app1/home.html',{'sender_email': sender_email})

    else:
        print('at home page')
        return render(request, 'app1/home.html', {})

def login(request):
    return render(request, 'app1/login.html')