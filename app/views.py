from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.decorators import *
from django.contrib.auth.models import Group
from app.models import *


# Create your views here.

def login_view(request):
  return render(request, "log-in.html", {})

def signup_view(request):
  form = CreateUserForm()
  
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():

      user = form.save()

      username = form.cleaned_data.get('username')
      messages.success(request, 'Your account was successfully created ' + username)
      # group = Group.objects.get(name='customer')
      # user.groups.add(group)
      return redirect('login')
  return render(request, 'sign-up.html', {"form": form})