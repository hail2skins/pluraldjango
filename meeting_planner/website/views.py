from django.shortcuts import render
from django.http import HttpResponse

# Add the Meeting model
from meetings.models import Meeting

# Create your views here.
# Add a welcome view
def welcome(request):
    return render(
        request, template_name="website/welcome.html",
        context={"num_meetings": Meeting.objects.count()},
        )

# Add about page with some text
def about(request):
    return HttpResponse("This is a meeting planner project created using Django.")
