from django.shortcuts import render

# Create your views here.

def login_view(request):
  return render(request, "log-in.html", {})

def signup_view(request):
  return render(request, 'sign-up.html', {})