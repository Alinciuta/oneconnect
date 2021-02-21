from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from app1.models import Events
from app2.forms import QuestionForm
from app2.models import Question


class Questions(ListView):
    model = Question
    template_name = 'app1/events/event_live.html'
    context_object_name = 'all_questions'

    def get_context_data(self, *, object_list=None, **kwargs):
        intrebari = super(Questions, self).get_context_data()
        return intrebari
