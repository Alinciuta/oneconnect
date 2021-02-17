from django import forms
from app2.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('name', 'email', 'body')
