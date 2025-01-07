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
  message = forms.CharField(max_length=250, widget=forms.Textarea)
  img = forms.ImageField(required=False)

  def __init__(self, *args, **kwargs):
    super(ChatBox, self).__init__(*args, **kwargs)
    for visible in self.visible_fields():
      if visible.name == 'message':
        visible.field.widget.attrs['name'] = "enterMessage"
        visible.field.widget.attrs['id'] = "enterMessage"
        visible.field.widget.attrs['cols'] = "30"
        visible.field.widget.attrs['rows'] = "2"
        visible.field.widget.attrs['placeholder'] = "Say message..."


class Apply(forms.Form):
  business = forms.CharField(max_length=200)
  picture = forms.ImageField()

class GetServer(forms.Form):
  server = forms.CharField(max_length=200)