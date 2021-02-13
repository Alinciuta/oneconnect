from django import forms
from django.forms import TextInput, Textarea, Select
from django.http import HttpResponse

from app1.models import Events


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['eventname', 'banner', 'data', 'eventagenda', 'eventdescription', 'event_type']

        widgets = {
            'eventname': TextInput(attrs={'placeholder': 'eventname', 'class': 'form-control'}),
            'banner': TextInput(attrs={'placeholder': 'banner', 'class': 'form-control'}),
            'data': TextInput(attrs={'placeholder': 'data', 'class': 'form-control'}),
            'eventagenda': Textarea(attrs={'placeholder': 'eventagenda', 'class': 'form-control'}),
            'eventdescription': Textarea(attrs={'placeholder': 'eventdescription', 'class': 'form-control'}),
            'event_type': Select(attrs={'placeholder': 'event_type', 'class': 'form-control'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        evname_val = cleaned_data.get('eventname')
        evdata_val = cleaned_data.get('eventdata')
        if self.pk:
            if Events.objects.filter(eventname=evname_val, eventdata=evdata_val).exclude(id=self.pk).exists():
                msg = 'Event already added'
                self._errors['city'] = self.error_class([msg])
        else:
            if Events.objects.filter(eventname=evname_val, eventdata=evdata_val).exists():
                msg = 'Event already added'
                self._errors['eventname'] = self.error_class([msg])
        return cleaned_data
