# from django import forms
# from django.forms import TextInput
# from app1.models import Events
#
#
# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Events
#         fields = ['eventname', 'banner', 'data', 'eventdescription', 'event_type']
#
#         widgets = {
#             'eventname': TextInput(attrs={'placeholder': 'Event name', 'class': 'form-control'}),
#             'banner': TextInput(attrs={'placeholder': 'Banner', 'class': 'form-control'}),
#             'data':
#             'eventdescription': TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}),
#             'event_type': Select(attrs={'class': 'form-control'}),
#         }
#
#     def __init__(self, pk, *args, **kwargs):
#         super(LocationForm, self).__init__(*args, **kwargs)
#         self.pk = pk
#
#     def clean(self):
#         cleaned_data = self.cleaned_data
#         city_val = cleaned_data.get('city')
#         country_val = cleaned_data.get('country')
#         if self.pk:
#             if Location.objects.filter(city=city_val, country=country_val).exclude(id=self.pk).exists():
#                 msg = 'City and country already exist'
#                 self._errors['city'] = self.error_class([msg])
#         else:
#             if Location.objects.filter(city=city_val, country=country_val).exists():
#                 msg = 'City and country already exist'
#                 self._errors['city'] = self.error_class([msg])
#         return cleaned_data