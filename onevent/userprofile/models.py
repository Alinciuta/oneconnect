from django.contrib.auth.models import User
from django.db import models
from django import forms


class UserExtend(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False, unique=True)
    username = models.CharField(max_length=200, blank=False, unique=True)
    for_event = models.ForeignKey('app1.Events', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
