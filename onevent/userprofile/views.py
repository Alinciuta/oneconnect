import string
from random import random
from string import punctuation

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import UpdateView, CreateView

from userprofile.forms import NewAccountForm
from userprofile.models import UserExtendE


class CreateUser(CreateView):
    form_class = NewAccountForm
    model = UserExtendE
    template_name = 'app1/events_form.html'

    def get_form_kwargs(self):
        kwargs = super(CreateUser, self).get_form_kwargs()
        kwargs.update({'pk': None, 'state': 'create'})
        return kwargs

    def form_valid(self, form):
        print(form.errors)
        if form.is_valid():
            form.save(commit=False)
        return super(CreateUser, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(CreateUser, self).form_invalid(form)

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + punctuation) for _ in range(8))
        try:
            user_instance = User.objects.get(id=self.object.id)
            user_instance.set_password(psw)
            user_instance.save()
            content_email = f'Your username and password: {user_instance.username} {psw}'
            msg_html = render_to_string('emails/invite_user.html', {'content_email': str(content_email)})
            msg = EmailMultiAlternatives(subject='Invite', body=content_email, from_email='contact@test.ro', to=[user_instance.email])
            msg.attach_alternative(msg_html, 'text/html')
            msg.send()
        except Exception:
            pass
        return reverse('login')


class UpdateProfile(LoginRequiredMixin, UpdateView):
    fields = '__all__'
    model = User
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reversed()