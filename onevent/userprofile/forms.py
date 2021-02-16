from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, Select
from userprofile.models import UserExtend


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'username', 'for_event']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email address', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'for_event': Select(attrs={'placeholder': 'Interested in', 'class': 'form-control'}),
        }

    def __init__(self, pk, state, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.pk = pk
        self.state = state

    def clean(self):
        cleaned_data = self.cleaned_data
        email_val = cleaned_data.get('email')
        username_val = cleaned_data.get('username')
        if self.state == 'create':
            if User.objects.filter(email=email_val).exists():
                msg = 'Email already in our database. Already have an account? Go to log-in page'
                self._errors['email'] = self.error_class([msg])
            if User.objects.filter(username=username_val).exists():
                msg = 'Username already in our database. Already have an account? Go to log-in page'
                self._errors['username'] = self.error_class([msg])
        elif self.state == 'update':
            if User.objects.filter(email=email_val).exclude(id=self.pk).exists():
                msg = 'Email already in our database. Already have an account? Go to log-in page'
                self._errors['email'] = self.error_class([msg])
            if User.objects.filter(username=username_val).exclude(id=self.pk).exists():
                msg = 'Username already in our database. Already have an account? Go to log-in page'
                self._errors['username'] = self.error_class([msg])
