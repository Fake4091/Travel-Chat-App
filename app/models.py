from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.


class Server(models.Model):
    name = models.CharField(max_length=100)


class Channel(models.Model):
    name = models.CharField(max_length=100)
    server = models.ForeignKey(
        Server,
        on_delete=models.CASCADE,
        related_name="channels",
        related_query_name="channel",
    )


class Role(models.Model):
    name = models.CharField(max_length=100)
# allows for different roles on a per channel basis
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE,
        related_name="roles",
        related_query_name="role",
    )

# list off permissions as booleans, then later we create instances of this class
# e.g. banPerms = models.BooleanField(), kickPerms = models.BooleanField(), etc.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    servers = models.ManyToManyField(
        Server, related_name="users", related_query_name="user"
    )
    roles = models.ManyToManyField(
        Role, related_name="users", related_query_name="user",
    )
    


class Message(models.Model):
    text = models.TextField()
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="messages"
    )
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="messages")
    date_time = models.DateTimeField()

class Business(models.Model):

    business = models.CharField(max_length=200)

    picture = models.ImageField()

    server = models.CharField(max_length=200)

    channel = models.CharField(max_length=200)