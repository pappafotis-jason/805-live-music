from django.db import models
from django.contrib.gis.db import models as gis_models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    location = gis_models.PointField()
    city = models.CharField(max_length=50, default='Panama City Beach')

    def __str__(self):
        return self.name

class Act(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    act = models.ForeignKey(Act, on_delete=models.CASCADE)
    details = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.venue}"
