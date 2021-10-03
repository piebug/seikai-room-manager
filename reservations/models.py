from rooms.models import Room
from django.db import models
from django.conf import settings


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    other_occupants = models.TextField()
    purpose = models.TextField()