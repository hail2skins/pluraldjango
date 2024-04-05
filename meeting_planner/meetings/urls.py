from django.urls import path # Import the path function
from meetings import views # Import the views module from the meetings app

urlpatterns = [
    path('<int:id>', views.detail, name='detail'), # Add a URL pattern for the detail view
    path('rooms', views.rooms, name='rooms'), # Add a URL pattern for the rooms view
]