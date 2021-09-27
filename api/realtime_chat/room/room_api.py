from rest_framework import generics
from realtime_chat.models import Room
from .room_serializers import RoomSerializer


__all__ = ['RoomView']

class RoomAPI(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
