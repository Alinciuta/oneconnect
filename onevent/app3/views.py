from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView

from app3.forms import FeedbackForm
from app3.models import Feedback


class FeedbackFormAdd(CreateView):
    model = Feedback
    fields = ['name', 'email', 'eveniment', 'q1', 'q2', 'q3', 'q4', 'q5', 'comments']
    template_name = 'app3/feedback_form.html'

    def get_success_url(self):
        return reverse('app3:feedback_complete')


# class Raspunsuri(ListView):
#     model = FeedbackForm
#     template_name = 'app3/feedback_index.html'
#     context_object_name = 'all_feedback'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         data = super(Raspunsuri, self).get_context_data()
#         return data


def completed(request):
    return render(request, 'app3/feedback_complete.html')