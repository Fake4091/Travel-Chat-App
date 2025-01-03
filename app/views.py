from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from app.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.decorators import *
from django.contrib.auth.models import Group
from app.models import *
from django.contrib.auth.models import User
import datetime


# Sign-up / Log-in area -----------------------------------------------------------------------------------


@unauthenticated_user
def signup_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            profile = Profile(user=user)
            profile.save()

            username = form.cleaned_data.get("username")
            messages.success(
                request, "Your account was successfully created " + username
            )
            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            return redirect("login")
    return render(request, "sign-up.html", {"form": form})


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username OR password is incorrect.")
    return render(request, "log-in.html", {})


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")


# ---------------------------------------------------------------------------------------------------


@login_required(login_url="login")
def home_view(request):
    servers_user_in = request.user.profile.servers.all()

    return render(request, "home.html", {"servers": servers_user_in})


def home_server_view(request, server):
    server_needed = Server.objects.get(name=server)
    channels = Channel.objects.filter(server=server_needed)

    return render(
        request, "home-server.html", {"server": server_needed, "channels": channels}
    )


def home_channel_view(request, server, channel):
    channel_needed = Channel.objects.get(name=channel)
    print(channel_needed.name)
    form = ChatBox(request.POST)

    if form.is_valid():
        message = form.cleaned_data["message"]

        new_message = Message(
            text=message,
            channel=channel_needed,
            user_profile=request.user.profile,
            date_time=datetime.datetime.now(),
        )
        new_message.save()

    messages = Message.objects.filter(channel=channel_needed)

    return render(
        request,
        "home-channel.html",
        {"form": form, "server": server, "channel": channel, "messages": messages},
    )


@login_required(login_url="login")
def join_server_view(request):
    print(Server.objects.all())
    form = ServerName(request.GET)
    data = Server.objects.all()
    if form.is_valid():
        server_name = form.cleaned_data["server_name"]
        characters = len(server_name)
        data_wanted = []
        for i in data:
            if i.name[:characters] == server_name:
                data_wanted.append(i)
            return render(request, "join.html", {"data": data_wanted, "form": form})

    return render(request, "join.html", {"data": data, "form": form})


@login_required(login_url="login")
def join_success_view(request, server_name):
    request.user.profile.servers.add(Server.objects.get(name=server_name))
    return render(request, "join_success.html", {"name": server_name})
