from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app1.models import Events
from app1.forms import EventForm


class HomeIndex(ListView):
    model = Events
    template_name = 'app1/events_index.html'
    context_object_name = 'all_events'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(HomeIndex, self).get_context_data()
        return data


class EventFormAdd(CreateView):
    model = Events
    fields = ['eventname', 'banner', 'eventdate', 'eventagenda', 'eventdescription', 'event_type', 'video_url', 'slug']
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

    def get_success_url(self):
        return reverse('app1:events')


class UpdateEventsView(LoginRequiredMixin, UpdateView):
    model = Events
    form_class = EventForm
    template_name = 'app1/events_form.html'

    def get_form_kwargs(self):
        kwargs = super(UpdateEventsView, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk']})
        return kwargs

    def get_success_url(self):
        return reverse('app1:home')


class EventzDetailView(DetailView):
    model = Events
    template_name = 'app1/events/event_live.html'
