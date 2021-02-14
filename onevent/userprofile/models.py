from django.contrib.auth.models import User
from django.db import models


class UserExtendE(User):

    for_event = models.ForeignKey('app1.Events', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
