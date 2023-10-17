from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login

from .forms import *


class RegistrationView(FormView):
    form_class = SingUpForm
    template_name = 'registration/user_registration.html'
    success_url = reverse_lazy('user_profile')
    extra_context = {'title': 'Регистрация'}

    def form_valid(self, form):
        new_user: Profile = form.save()
        login(self.request, new_user)
        return super(RegistrationView, self).form_valid(form)
