from django.db import models
from django.urls import reverse

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
    short = models.CharField(max_length=30, blank=False, unique=True, null=True)
    video_url = models.CharField(max_length=1000, blank=False, unique=True, null=True)

    def __str__(self):
        return f"{self.eventname} - {self.eventdate}"

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])


class Question(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.author}: {self.content}"

    def get_absolute_url(self):
        return reverse('event_detail', args=[str(self.id)])