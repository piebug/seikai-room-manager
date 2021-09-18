from django.urls import path

from .views import RoomsList, RoomDetails
from .apps import RoomsConfig

app_name = RoomsConfig.name
urlpatterns = [
    path('<int:pk>/details', RoomDetails.as_view(), name='room_details'),
    path('', RoomsList.as_view(), name='rooms_list'),
]
