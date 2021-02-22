from django.views.generic import ListView
from app2 import models
from app2.models import Question


class Questions(ListView):
    model = Question
    template_name = 'app1/event_questions.html'
    context_object_name = 'all_questions'
    objects = models.Question
