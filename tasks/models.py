from django.db import models
from users.models import Worker


class TaskType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField()

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default=MEDIUM,
    )

    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)

    assignees = models.ManyToManyField(Worker, related_name='assigned_tasks')

    def __str__(self):
        return self.name
