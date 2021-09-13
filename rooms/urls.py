from django.urls import path

from .views import RoomsList
from .apps import RoomsConfig

app_name = RoomsConfig.name
urlpatterns = [
    path('', RoomsList.as_view(), name='rooms_list'),
]
