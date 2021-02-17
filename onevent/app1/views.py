from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app1.models import Events
from app1.forms import EventForm
from app2.forms import QuestionForm
from app2.models import Question


class HomeIndex(ListView):
    model = Events
    template_name = 'app1/events_index.html'
    context_object_name = 'all_events'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(HomeIndex, self).get_context_data()
        return data


class EventFormAdd(CreateView):
    model = Events
    fields = ['eventname', 'banner', 'eventdate', 'eventagenda', 'eventdescription', 'event_type', 'video_url']
    template_name = 'app1/events_form.html'

    def get_success_url(self):
        return reverse('app1:events')


def contact1(request):
    return render(request, 'contact.html')


def acasa(request):
    return render(request, 'acasa.html')


class EventsDeleteView(DeleteView):
    model = Events

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
        return reverse('app1:events')


class EventzDetailView(CreateView):
    model = Question
    template_name = 'app1/events/event_live.html'
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        data = super(EventzDetailView, self).get_context_data(**kwargs)
        data['object'] = Events.objects.get(id=self.request.GET.get('e'))
        return data

    def form_valid(self, form):
        if form.is_valid():
            question = form.save(commit=False)
            question.eveniment_id = Events.objects.get(id=self.request.GET.get('e')).id
            question.save()
        return redirect(f"/?e={self.request.GET.get('e')}")

    def get_success_url(self):
        return reverse('app1:event_detail')
