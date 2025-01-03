from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']

class ServerName(forms.Form):
  server_name = forms.CharField(max_length=100)

class CreateServer(forms.Form):
  server_name = forms.CharField(max_length=100)

class ChatBox(forms.Form):
  message = forms.CharField(max_length=250)