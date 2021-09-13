from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Room


class RoomsList(ListView):
    """Lists all the rooms in the school that can be reserved by students and staff"""
    model = Room
    template_name = 'rooms/rooms_list.html'


class RoomDetails(DetailView):
    """"""
    model = Room
    template_name = 'rooms/room_details.html'
