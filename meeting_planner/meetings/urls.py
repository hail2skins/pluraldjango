from django.urls import path # Import the path function
from meetings import views # Import the views module from the meetings app

urlpatterns = [
    path('<int:id>', views.detail, name='detail'), # Add a URL pattern for the detail view
    path('rooms', views.rooms, name='rooms'), # Add a URL pattern for the rooms view
    path('new', views.new, name='new'), # Add a URL pattern for the new view
    path('edit/<int:id>', views.edit, name='edit'), # Add a URL pattern for the edit view
    path('delete/<int:id>', views.delete, name='delete'), # Add a URL pattern for the delete view
]