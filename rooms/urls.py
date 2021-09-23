from django.urls import path

from .apps import RoomsConfig
from .views import RoomsList, RoomDetails

app_name = RoomsConfig.name
urlpatterns = [
    path('<int:pk>/details', RoomDetails.as_view(), name='room_details'),
    path('', RoomsList.as_view(), name='rooms_list'),
]
