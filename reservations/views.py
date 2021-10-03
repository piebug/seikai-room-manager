from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Reservation


class ReservationList(ListView):
    """Lists all the reservations associated with a room or a user"""
    model = Reservation
    template_name = 'reservations/reservation_list.html'


class ReservationDetails(DetailView):
    """Renders a page dedicated to a single room that can be reserved by students and staff"""
    model = Reservation
    template_name = 'reservations/reservation_details.html'
