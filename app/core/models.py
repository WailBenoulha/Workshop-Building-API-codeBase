from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)