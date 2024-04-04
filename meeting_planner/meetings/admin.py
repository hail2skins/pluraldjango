from django.contrib import admin

# Import your classes from models.py
from meetings.models import Meeting # Import the Meeting class

# Register your models here.
admin.site.register(Meeting) # Register the Meeting class with the admin site
