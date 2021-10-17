from django.urls import path

from .views import ReservationList, ReservationDetails
from .apps import ReservationsConfig

app_name = ReservationsConfig.name
urlpatterns = [
    path('<int:pk>/details/', ReservationDetails.as_view(), name='reservation_details'),
    path('', ReservationList.as_view(), name='reservation_list'),
]
