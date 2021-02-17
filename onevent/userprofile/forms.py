from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, Select, ModelChoiceField
from app1.models import Events
from userprofile.models import UserExtend


class NewAccountForm(forms.ModelForm):

    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'username', 'customer']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Email address', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Username of user', 'class': 'form-control'}),
            'customer': Select(attrs={'placeholder': 'Username of user', 'class': 'form-control'}),
        }

    def __init__(self, pk, state, *args, **kwargs):
        super(NewAccountForm, self).__init__(*args, **kwargs)
        self.pk = pk
        self.state = state
        if self.state != 'create':
            print(UserExtend.objects.get(id=self.pk).customer.id)
            self.fields['customer'] = ModelChoiceField(
                queryset=Events.objects.filter(id=UserExtend.objects.get(id=self.pk).customer.id))
            self.initial['customer'] = Events.objects.get(id=UserExtend.objects.get(id=self.pk).customer.id)
            self.fields['customer'].widget.attrs['class'] = 'form-control'


    def clean(self):
        cleaned_data = self.cleaned_data
        email_val = cleaned_data.get('email')
        username_val = cleaned_data.get('username')
        if self.state == 'create':
            if User.objects.filter(email=email_val).exists():
                msg = 'Emailul deja exista, te rugam sa alegi un alt email'
                self._errors['email'] = self.error_class([msg])
            if User.objects.filter(username=username_val).exists():
                msg = 'Username deja exista, te rugam sa alegi un alt email'
                self._errors['username'] = self.error_class([msg])
        elif self.state == 'update':
            if User.objects.filter(email=email_val).exclude(id=self.pk).exists():
                msg = 'Emailul deja exista, te rugam sa alegi un alt email'
                self._errors['email'] = self.error_class([msg])
            if User.objects.filter(username=username_val).exclude(id=self.pk).exists():
                msg = 'Username deja exista, te rugam sa alegi un alt email'
                self._errors['username'] = self.error_class([msg])
