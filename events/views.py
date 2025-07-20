from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from .models import Event
from .forms import EventForm

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map_view')
        else:
            print("Form errors:", form.errors)  # Optional debug
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

@cache_page(60 * 15)  # Cache for 15 minutes
def map_view(request):
    events = Event.objects.all()  # Fetch all events
    print("Events queried:", events)  # Debug output
    return render(request, 'events/map.html', {'events': events})

# Expand with calendar view later
