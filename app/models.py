from django.db import models
from django.contrib.auth.models import User
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
    # allows for different roles on a per channel basis
    channel = models.ManyToManyField(
        Server,
        related_name="roles",
        related_query_name="role",
    )
    # list off permissions as booleans, then later we create instances of this class
    # e.g. banPerms = models.BooleanField(), kickPerms = models.BooleanField(), etc.


class WebUser(models.Model):
    name = models.CharField(max_length=100)
    servers = models.ManyToManyField(
        Server, related_name="users", related_query_name="user"
    )
    roles = models.ManyToManyField(
        Role, related_name="users", related_query_name="user"
    )


class Message(models.Model):
    text = models.TextField()
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="messages"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages")
