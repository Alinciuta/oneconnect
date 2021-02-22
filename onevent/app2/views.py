from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from app2 import models
from app2.forms import QuestionForm
from app2.models import Question


class Questions(ListView):
    model = Question
    template_name = 'app1/event_questions.html'
    context_object_name = 'all_questions'
    objects = models.Question

    # def get_context_data(self, **kwargs):
    #     data = super(Questions, self).get_context_data(**kwargs)
    #     data = Questions.objects.filter(eveniment_id=self.request.GET.get('e'))
    #     return data

