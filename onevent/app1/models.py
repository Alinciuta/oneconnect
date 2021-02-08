from django.db import models

# Create your models here.

et_choices = (('Virtual', 'Virtual'),
               ('Live', 'Live'),
               ('Hybrid', 'Hybrid'))

class Events(models.Model):

    eventname = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='bannere', null=True)
    eventdate = models.DateTimeField('data')
    eventdescription = models.TextField()
    event_type = models.CharField(max_length=50, choices=et_choices)

    def __str__(self):
        return f"{self.banner} - {self.eventname} - {self.eventdate}"
