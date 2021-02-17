from django.contrib.auth.models import User
from django.db import models
from django import forms
from app1.models import Events


class UserExtend(User):

    customer = models.ForeignKey('app1.Events', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.customer.name}'


class Logs(models.Model):

    action_choice = (('created', 'created'), ('updated', 'updated'), ('refresh', 'refresh'))

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(UserExtend, on_delete=models.CASCADE)
    for_event = models.ForeignKey(Events, on_delete=models.CASCADE)

