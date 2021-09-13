from django.shortcuts import render
from django.views.generic import ListView

from .models import Room

class RoomsList(ListView):
    """"""
    model = Room
    template_name = 'rooms/rooms_list.html'