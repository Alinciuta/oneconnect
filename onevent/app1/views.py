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


class HomeIndex(ListView):
    model = Events
    template_name = 'app1/events_index.html'
    context_object_name = 'all_events'


class EventFormAdd(CreateView):
    model = Events
    fields = ['eventname', 'banner', 'eventdate', 'eventagenda', 'eventdescription', 'event_type']
    template_name = 'app1/events_form.html'

    # def get_form_kwargs(self):
    #     kwargs = super(EventFormAdd, self).get_form_kwargs()
    #     kwargs.update({'pk': None})
    #     return kwargs

    def get_success_url(self):
        return reverse('app1:events')


def contact1(request):
    return render(request, 'contact.html')


def acasa(request):
    return render(request, 'acasa.html')


def preventia_sinuciderii(request):
    return render(request, 'app1/events/preventia_sinuciderii.html')


class EventsDeleteView(DeleteView):
    model = Events
    success_url = "/"

    def get_success_url(self):
        return reverse('app1:events')


class UpdateEventsView(UpdateView):
    model = Events
    fields = ['eventname', 'banner', 'eventdate', 'eventagenda', 'eventdescription', 'event_type']
    template_name = 'app1/events_form.html'

    def get_form_kwargs(self):
        kwargs = super(UpdateEventsView, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs

    def get_success_url(self):
        return reverse('app1:events')
