from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    contents = models.TextField()
    capacity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(350)])
