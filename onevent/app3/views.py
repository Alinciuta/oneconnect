from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView
from app3.models import Feedback


class FeedbackFormAdd(CreateView):
    model = Feedback
    fields = ['name', 'email', 'eveniment', 'q1', 'q2', 'q3', 'q4', 'q5', 'comments']
    template_name = 'app3/feedback_form.html'

    def get_success_url(self):
        return reverse('app3:feedback_complete')


def completed(request):
    return render(request, 'app3/feedback_complete.html')