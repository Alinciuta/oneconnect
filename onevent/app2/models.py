from django.db import models

# Create your models here.
from app1.models import Events


class Question(models.Model):
    eveniment = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='questions')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Question {} by {}'.format(self.body, self.name)
