from django.db import models

from datetime import time # Import the time class from the datetime module

# Create your models here.
# Add meeting class to models.py
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey("Room", on_delete=models.CASCADE) # Add a foreign key to the Room model

    def __str__(self):
        return f"{self.title} on {self.date} at {self.start_time} on {self.date}" # Return a string representation of the meeting object in the admin site
    
# Add model called Room
# Room has name, and floor_number and a room_number
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name} on floor {self.floor_number} room {self.room_number}" # Return a string representation of the room object in the admin site