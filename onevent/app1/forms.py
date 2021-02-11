from django import forms
from django.forms import TextInput, Textarea, Select
from app1.models import Events


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['eventname', 'banner', 'data', 'eventdescription', 'event_type']

        widgets = {
            'eventname': TextInput(attrs={'placeholder': 'eventname', 'class': 'form-control'}),
            'banner': TextInput(attrs={'placeholder': 'banner', 'class': 'form-control'}),
            'data': TextInput(attrs={'placeholder': 'data', 'class': 'form-control'}),
            'eventdescription': Textarea(attrs={'placeholder': 'eventdescription', 'class': 'form-control'}),
            'event_type': Select(attrs={'placeholder': 'event_type', 'class': 'form-control'}),
        }

    def __init__(self, pk, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.pk = pk

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     city_val = cleaned_data.get('city')
    #     country_val = cleaned_data.get('country')
    #     if self.pk:
    #         if Events.objects.filter(city=city_val, country=country_val).exclude(id=self.pk).exists():
    #             msg = 'City and country already exist'
    #             self._errors['city'] = self.error_class([msg])
    #     else:
    #         if Location.objects.filter(city=city_val, country=country_val).exists():
    #             msg = 'City and country already exist'
    #             self._errors['city'] = self.error_class([msg])
    #     return cleaned_data