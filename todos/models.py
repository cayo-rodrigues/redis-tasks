from django.db import models

# Create your models here.


class Todo(models.Model):
    class PriorityChoices(models.IntegerChoices):
        EXTRA = 1
        LOW = 2
        MID = 3
        HIGH = 4
        URGENT = 5

    task_description = models.TextField()
    priority = models.PositiveSmallIntegerField(
        choices=PriorityChoices.choices, null=True, blank=True, default=None
    )
    doing = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
