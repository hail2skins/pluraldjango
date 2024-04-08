from django.shortcuts import render, get_object_or_404, redirect # Import the render, get_object_or_404, and redirect functions
from django.forms import modelform_factory # Import the modelform_factory function allowing Django to create forms from models

# Add the Meeting model
from meetings.models import Meeting, Room

# Create your views here.
def detail(request, id):
    #meeting = Meeting.objects.get(pk=id)
    meeting = get_object_or_404(Meeting, pk=id) # Use get_object_or_404 to get the meeting
    return render(
        request, template_name="meetings/details.html",
        context={"meeting": meeting},
    )
    
# Add a new page that shows a list of all room objects
def rooms(request):
    return render(
        request, template_name="meetings/rooms.html",
        context={"rooms": Room.objects.all()},
    )

# Add a new view allowing addition of meetings
MeetingForm = modelform_factory(Meeting, exclude=[]) # Create a form from the Meeting model
def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid(): # Check if the form is valid of each field
            form.save()
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", 
                  {"form": form})
    
# Add a new view allowing editing of meetings
def edit(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        form = MeetingForm(request.POST, instance=meeting)
        if form.is_valid():
            form.save()
            return redirect("detail", id=id)
    else:
        form = MeetingForm(instance=meeting)
    return render(request, "meetings/edit.html", 
                  {"form": form, "meeting": meeting})
    
# Add a new view allowing deletion of meetings
def delete(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    if request.method == "POST":
        meeting.delete()
        return redirect("home")
    return render(request, "meetings/confirm_delete.html", 
                  {"meeting": meeting})