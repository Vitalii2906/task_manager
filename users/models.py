from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    groups = models.ManyToManyField(Group, related_name='workers')
    user_permissions = models.ManyToManyField(Permission, related_name='workers')

    def __init__(self, *args, **kwargs):
        position = kwargs.pop('position', None)
        super().__init__(*args, **kwargs)
        
        if position:
            self.position = position

    def __str__(self) -> str:
        return self.username
