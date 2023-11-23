from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import Worker, Position

class WorkerSignUpForm(UserCreationForm):
    position = forms.ModelChoiceField(queryset=Position.objects.all(), label='Position')

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + ('position',)