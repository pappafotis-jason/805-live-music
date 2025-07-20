from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from .models import Event
from .forms import EventForm
from datetime import datetime

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map_view')
        else:
            print("Form errors:", form.errors)
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})

@cache_page(60 * 1)
def map_view(request):
    date_str = request.GET.get('date')
    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            events = Event.objects.filter(date_time__date=date)
        except ValueError:
            events = Event.objects.all()
    else:
        events = Event.objects.all()
    print("Map view rendered with events:", list(events))  # Debug output
    return render(request, 'events/map.html', {'events': events})

# Expand with calendar view later
