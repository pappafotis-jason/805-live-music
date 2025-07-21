from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-event/', views.add_event, name='add_event'),
    path('map/', views.map_view, name='map_view'),
]
