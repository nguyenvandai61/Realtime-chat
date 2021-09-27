# urlpatterns
from realtime_chat.emotion.emotion_api import EmotionAPI
from realtime_chat.user.user_api import ListUserAPI, RegisterUserAPI
from django.urls import path
from .room.room_api import RoomAPI


urlpatterns = [
    path('register/', RegisterUserAPI.as_view(), name='register_user'),
    path('user/', ListUserAPI.as_view(), name='room_api'),
    path('emotion/', EmotionAPI.as_view(), name='emotion_api'),
    path('room/', RoomAPI.as_view(), name='index'),
    
]