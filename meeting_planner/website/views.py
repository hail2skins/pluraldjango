from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Add a welcome view
def welcome(request):
    return HttpResponse("Welcome to the meeting planner!")

# Add about page with some text
def about(request):
    return HttpResponse("This is a meeting planner project created using Django.")
