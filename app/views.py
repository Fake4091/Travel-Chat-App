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


# Create your views here.

def lobby_view(request):
    return render(request, "lobby.html")

# Sign-up / Log-in area -----------------------------------------------------------------------------------

@unauthenticated_user
def signup_view(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():

            form.save()
            profile = Profile(user=User.objects.get(username=form.cleaned_data.get("username")))
            profile.save()

            username = form.cleaned_data.get("username")
            messages.success(
                request, "Your account was successfully created " + username
            )
            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            return redirect("login")
    return render(request, "log-in.html", {"form": form})


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
    servers_user_in = request.user.profile.servers.all()


    return render(
        request, "home-server.html", {"servers": servers_user_in, "server": server_needed, "channels": channels}
    )


def home_channel_view(request, server, channel):
    channel_needed = Channel.objects.get(name=channel)
    profile_object = Profile.objects.get(user=request.user)
    servers_user_in = request.user.profile.servers.all()


    try: 
        if profile_object.roles.get(channel=channel_needed).name == 'Business Owner' :
            print('Business Owner')
        elif profile_object.roles.get(channel=channel_needed).name == 'Tourist':
            print('Tourist')
    except:
        new_role = Role(name='Tourist', channel=channel_needed)
        new_role.save()
        profile_object.roles.add(new_role)

    role = profile_object.roles.get(channel=channel_needed).name
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
        {"servers": servers_user_in, "form": form, "server": server, "channel": channel, "messages": messages, "role": role},
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
            print(i.name[:characters] == server_name) 
            print(i.name[:characters] == server_name) 
            if i.name[:characters] == server_name:
                print(i)
                print(i)
                data_wanted.append(i)
        return render(request, "join.html", {"data": data_wanted, "form": form})
        return render(request, "join.html", {"data": data_wanted, "form": form})

    return render(request, "join.html", {"data": data, "form": form})


@login_required(login_url="login")
def join_success_view(request, server_name):
    request.user.profile.servers.add(Server.objects.get(name=server_name))

    return redirect('home')

@login_required(login_url="login")
def roles_page_view(request):
    roles = Role.objects.all()
  


    return render(request, 'roles-page.html', {"roles": roles})

    return redirect('home')

@login_required(login_url="login")
def roles_page_view(request):
    roles = Role.objects.all()
  


    return render(request, 'roles-page.html', {"roles": roles})

def role_apply_view(request):
    servers_user_in = request.user.profile.servers.all()
    form = ServerName(request.GET)
    data = Server.objects.all()
    if form.is_valid():
        server_name = form.cleaned_data["server_name"]
        characters = len(server_name)
        data_wanted = []
        for i in data:
            print(i.name[:characters] == server_name) 
            print(i.name[:characters] == server_name) 
            if i.name[:characters] == server_name:
                print(i)
                print(i)
                data_wanted.append(i)
        return render(request, "join.html", {"data": data_wanted, "form": form})
    
    return render(request, 'role-apply.html', {"form": form, "data": data})

def role_apply_server_view(request, server):
    server_object = Server.objects.get(name=server)

    channels = Channel.objects.filter(server=server_object)



    return render(request, 'role-apply-server.html', {"server": server, "channels": channels})



def role_apply_channel_view(request, server, channel):

    form = Apply(request.POST, request.FILES)

    if form.is_valid():
        print("success")
        business = form.cleaned_data['business']
        picture = form.cleaned_data['picture']

        new_business = Business(business=business, picture=picture, server=server, channel=channel)
        new_business.save()
        return redirect("home")

    return render(request, 'role-apply-channel.html', {"server": server, "channel": channel, "form": form})