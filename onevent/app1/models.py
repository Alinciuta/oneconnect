from django.db import models

# Create your models here.
from django.db.models import options
from django.forms import forms, ModelForm, Textarea

et_choices = (('Virtual', 'Virtual'),
               ('Live', 'Live'),
               ('Hybrid', 'Hybrid'))


class Events(models.Model):
    eventname = models.CharField(max_length=200, unique=True)
    banner = models.ImageField(upload_to='bannere', null=True, blank=True)
    eventdate = models.CharField(max_length=200)
    eventdescription = models.TextField(default='')
    eventagenda = models.TextField(default='')
    event_type = models.CharField(max_length=50, choices=et_choices)

    def __str__(self):
        return f"{self.banner} - {self.eventname} - {self.eventdate}"


class Question(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=300)

    def __str__(self):
        return str(self.author)
