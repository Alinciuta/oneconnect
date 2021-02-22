import string
import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Permission
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import UpdateView, CreateView
from userprofile.forms import NewAccountForm
from userprofile.models import UserExtend


class UpdateProfile(LoginRequiredMixin, UpdateView):
    form_class = NewAccountForm
    model = UserExtend
    template_name = 'app1/events_form.html'

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_form_kwargs(self):
        kwargs = super(UpdateProfile, self).get_form_kwargs()
        kwargs.update({'pk': self.kwargs['pk'], 'state': 'update'})
        return kwargs

    def get_success_url(self):
        return reverse('app1:home')


punctuation = '!$%?#@'


class CreateNewUser(CreateView):
    form_class = NewAccountForm
    model = UserExtend
    template_name = 'app1/events_form.html'

    def get_form_kwargs(self):
        kwargs = super(CreateNewUser, self).get_form_kwargs()
        kwargs.update({'pk': None, 'state': 'create'})
        return kwargs

    def form_valid(self, form):
        print(form.errors)
        if form.is_valid():
            form.save(commit=False)
        return super(CreateNewUser, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(CreateNewUser, self).form_invalid(form)

    def get_success_url(self):
        psw = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + punctuation) for _ in range(8))
        try:
            user_instance = User.objects.get(id=self.object.id)
            user_instance.set_password(psw)
            user_instance.save()
            content_email = f'Your Login details are: {user_instance.username} - {psw}'
            msg_html = render_to_string('user_activation.html', {'content_email': str(content_email)})
            msg = EmailMultiAlternatives(subject='Account_activated', body=content_email, from_email='noreply@onevent.ro', to=[user_instance.email])
            msg.attach_alternative(msg_html, 'text/html')
            msg.send()
        except Exception:
            pass
        return reverse('login')

    # def permis(self, username):
    #     permission = Permission.objects.get(customer='customer')
    #     u = get_user_model().get(username=username)
    #     u.user_permissions.add(permission)
