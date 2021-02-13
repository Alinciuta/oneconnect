from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView


class UpdateProfile(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    model = User
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reversed()