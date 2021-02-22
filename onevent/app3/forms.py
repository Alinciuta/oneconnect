from django import forms
from django.forms import TextInput, Textarea, Select, ImageField, ClearableFileInput
from app3.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'eveniment', 'q1', 'q2', 'q3', 'q4', 'q5', 'comments']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}),
            'eveniment': Select(attrs={'placeholder': 'eveniment', 'class': 'form-control'}),
            'q1': Select(attrs={'placeholder': 'q1', 'class': 'form-control'}),
            'q2': Select(attrs={'placeholder': 'q2', 'class': 'form-control'}),
            'q3': Select(attrs={'placeholder': 'q3', 'class': 'form-control'}),
            'q4': Select(attrs={'placeholder': 'q4', 'class': 'form-control'}),
            'q5': Select(attrs={'placeholder': 'q5', 'class': 'form-control'}),
            'comments': Textarea(attrs={'placeholder': 'comments:', 'class': 'form-control'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.pk = pk
