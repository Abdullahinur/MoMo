import datetime as dt

from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserRegistrationForm

# Create your views here.


def main(request):
    title = 'this is a test message'
    date = dt.date.today()
    return render(request, 'main/main.html', {"date": date, "title": title})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'registration/user_exists.html')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
