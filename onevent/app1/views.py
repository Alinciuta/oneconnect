from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse

from app1.models import Events



class HomeIndex(LoginRequiredMixin, ListView):
    model = Events
    template_name = 'app1/events_index.html'
    context_object_name = 'all_events'

