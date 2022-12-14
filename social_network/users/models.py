import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    dislikes = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.body
