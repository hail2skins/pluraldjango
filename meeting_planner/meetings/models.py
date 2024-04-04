from django.db import models

from datetime import time # Import the time class from the datetime module

# Create your models here.
# Add meeting class to models.py
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} on {self.date} at {self.start_time} on {self.date}"