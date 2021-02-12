from datetime import datetime

from django.shortcuts import render

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import template

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app1.models import Events
from django.http import HttpResponse, HttpRequest
from django.http import HttpResponse
import requests


class HomeIndex(ListView):
    model = Events
    template_name = 'app1/events_index.html'
    context_object_name = 'all_events'


class EventFormAdd(CreateView):
    model = Events
    fields = ['eventname', 'banner', 'eventdate', 'eventdescription', 'event_type']
    template_name = 'app1/events_form.html'

    def get_success_url(self):
        return reverse('app1:events')


def contact1(request):
    return render(request, 'contact.html')


def acasa(request):
    return render(request, 'acasa.html')


class EventsDeleteView(DeleteView):
    model = Events
    success_url = "/"


# class UpdateEventsView(UpdateView):
#     model = Events
#     form_class = EventFormAdd
#     template_name = 'app1/events_form.html'
#
#     def get_form_kwargs(self):
#         kwargs = super(UpdateEventsView, self).get_form_kwargs()
#         kwargs.update({'pk': self.kwargs['pk']})
#         return kwargs
#
#     def get_success_url(self):
#         return reverse('app1:events')
