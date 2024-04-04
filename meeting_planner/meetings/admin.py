from django.contrib import admin

# Import your classes from models.py
from meetings.models import Meeting # Import the Meeting class
from meetings.models import Room # Import the Room class

# Register your models here.
admin.site.register(Meeting) # Register the Meeting class with the admin site
admin.site.register(Room) # Register the Room class with the admin site
