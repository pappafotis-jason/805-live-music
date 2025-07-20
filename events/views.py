from django.shortcuts import render

# Create your views here.
=======
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
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

@cache_page(60 * 15)  # Cache for 15 minutes using Redis
def map_view(request):
    events = Event.objects.all()
    return render(request, 'map.html', {'events': events})

# Expand with calendar view later
