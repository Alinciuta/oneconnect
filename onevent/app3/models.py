from django.db import models

# Create your models here.
from app1.models import Events

choices = (('Excelent', 'Excelent'),
               ('Good', 'Good'),
               ('Medium', 'Medium'),
               ('Insuficient', 'Insuficient'))

agree = (('Yes', 'Yes'),
               ('No', 'No'),
               ('N/A', 'N/A'))

class Feedback(models.Model):
    name = models.CharField('Full name', max_length=80)
    email = models.EmailField("Email")
    eveniment = models.ForeignKey(Events, on_delete=models.CASCADE)
    q1 = models.CharField('1. Did you learn anything participating in this event?', max_length=100, choices=agree, default='Yes')
    q2 = models.CharField('2. How would you rate the quality of speakers?', max_length=100, choices=choices, default='Yes')
    q3 = models.CharField("3. How would you rate the event's organization?", max_length=100, choices=choices, default='Yes')
    q4 = models.CharField("4. Would you attend other events organized online?", max_length=100, choices=agree, default='Yes')
    q5 = models.CharField("5. How to you rate the quality of the scientific content?", max_length=100, choices=choices, default='Yes')
    comments = models.TextField('Comments and suggestions:', max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
