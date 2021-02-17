from django.shortcuts import render, get_object_or_404


# Create your views here.
from app1.models import Events
from app2.forms import QuestionForm


def eveniment_detail(request, slug):
    template_name = 'app1/events/event_live.html'
    eveniment = get_object_or_404(Events, slug=slug)
    questions = eveniment.questions.filter(active=True)
    new_question = None
    if request.method == 'POST':
        question_form = QuestionForm(data=request.POST)
        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            new_question.post = eveniment
            new_question.save()
    else:
        question_form = QuestionForm()

    return render(request, template_name, {'questions': questions,
                                           'new_question': new_question,
                                           'question_form': question_form})
