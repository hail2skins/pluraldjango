from django.shortcuts import render, get_object_or_404

# Add the Meeting model
from meetings.models import Meeting

# Create your views here.
def detail(request, id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id) # Use get_object_or_404 to get the meeting
    return render(
        request, template_name="meetings/details.html",
        context={"meeting": meeting},
    )
