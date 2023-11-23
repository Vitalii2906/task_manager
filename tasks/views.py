from django.utils import timezone
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task

class TaskListView(ListView):
    model = Task
    paginate_by = 100  # if pagination is desired
    template_name = 'tasks/sign_up.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
