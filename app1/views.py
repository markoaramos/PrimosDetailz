import email
from email import message
from http import client
import re
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app1.models import UserProfile
from app1.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

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

def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # First get the username and password supplied
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)
            # If we have a user
            if user:
                # Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to homepage
                    return redirect("/dashboard/")
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(
                    username, password))
                return render(request, 'app1/login.html', {"login_form": LoginForm})
    else:
        # Nothing has been provided for username or password.
        return render(request, 'app1/login.html', {"login_form": LoginForm})

    return render(request, 'app1/login.html', {"login_form": LoginForm})

def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return redirect('/')

@login_required(login_url='/login/')
def dashboard(request):

    return render(request, 'app1/dashboard.html',{})