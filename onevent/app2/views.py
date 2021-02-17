from urllib import request

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from app1.models import Events
from app2.forms import QuestionForm
from app2.models import Question


class Questions(ListView):
    template_name = 'app1/events/event_live.html'

    def eveniment_detail(request, slug):
        eveniment = get_object_or_404(Events, slug=slug)
        questions = eveniment.questions
        if request.method == 'POST':
            question_form = QuestionForm(data=request.POST)
        else:
            question_form = QuestionForm()
        return render(request, 'app1/events/event_live.html', {'questions': questions, 'question_form': question_form})

    def get_context_data(self, **kwargs):
        data = super(Questions, self).get_context_data(**kwargs)
        data['intrebare'] = Question.objects.filter(question=self.request.get('e')).eveniment_id
        return data

    context_object_name = 'all_questions'
