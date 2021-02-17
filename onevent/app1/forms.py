from django import forms
from django.forms import TextInput, Textarea, Select, ImageField, ClearableFileInput
from app1.models import Events


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['eventname', 'banner', 'eventdate', 'eventagenda', 'eventdescription', 'event_type', 'video_url', 'slug']

        widgets = {
            'eventname': TextInput(attrs={'placeholder': 'Event Name', 'class': 'form-control'}),
            'banner': ClearableFileInput(attrs={'placeholder': 'Banner'}),
            'eventdate': TextInput(attrs={'placeholder': 'Event date', 'class': 'form-control'}),
            'eventagenda': Textarea(attrs={'placeholder': 'Agenda', 'class': 'form-control'}),
            'eventdescription': Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}),
            'event_type': Select(attrs={'placeholder': 'Event type', 'class': 'form-control'}),
            'video_url': TextInput(attrs={'placeholder': 'Event video', 'class': 'form-control'}),
            'slug': TextInput(attrs={'placeholder': 'Slug', 'class': 'form-control'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        evname_val = cleaned_data.get('eventname')
        evdate_val = cleaned_data.get('eventdate')
        if self.pk:
            if Events.objects.filter(eventname=evname_val, eventdate=evdate_val).exclude(id=self.pk).exists():
                msg = 'Event already added'
                self._errors['eventdate'] = self.error_class([msg])
        else:
            if Events.objects.filter(eventname=evname_val, eventdate=evdate_val).exists():
                msg = 'Event already added'
                self._errors['eventname'] = self.error_class([msg])
        return cleaned_data
