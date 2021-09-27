from rest_framework import serializers
from realtime_chat.models import Room

__all__ = ['RoomSerializer']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'