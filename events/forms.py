from django import forms
from .models import Event, Venue, Act

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

# Add VenueForm and ActForm similarly if needed for separate submissions
