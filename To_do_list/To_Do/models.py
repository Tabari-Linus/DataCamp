from datetime import datetime
from django.db import models

# Create your models here.
class Task(models.Model):
    task_to_do = models.CharField(max_length=200)
    complete = models.BooleanField(default="False")
    added_time = models.DateTimeField(datetime.now())
    