from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from app1.models import Events



class HomeIndex(ListView):
    model = Events
    template_name = 'app1/events_index.html'
    context_object_name = 'all_events'


class EventFormAdd(CreateView):
    model = Events
    fields = ['eventname', 'banner', 'eventdate', 'eventdescription', 'event_type']
    template_name = 'app1/events_form.html'

    def get_success_url(self):
        return reverse('app1:home')

