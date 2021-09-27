from realtime_chat.emotion.emotion_serializers import EmotionSerializer
from rest_framework import generics
from realtime_chat.models import Emotion

class EmotionAPI(generics.ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer
