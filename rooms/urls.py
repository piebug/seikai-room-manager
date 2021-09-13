from django.urls import path

from .views import RoomsList, RoomDetail
from .apps import RoomsConfig

app_name = RoomsConfig.name
urlpatterns = [
    path('', RoomsList.as_view(), name='rooms_list'),
    path('<int:pk>/details', RoomDetail.as_view(), name='room_details')
]
