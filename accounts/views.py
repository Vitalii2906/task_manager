from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import WorkerSignUpForm

from users.models import Worker

#LoginRequiredMixin,
class WorkerSignUpView(CreateView):
    model = Worker
    form_class = WorkerSignUpForm
    template_name = 'accounts/sign_up.html'
    #success_url = reverse_lazy('login')  # Redirect to login page
