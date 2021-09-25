# urlpatterns
from django.urls import path
from .room.room_api import RoomAPI


urlpatterns = [
    path('', RoomAPI.as_view(), name='index'),
]