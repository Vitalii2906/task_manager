from django.urls import path
from .views import WorkerSignUpView

urlpatterns = [
    path('', WorkerSignUpView.as_view(), name='sign-up'),
]