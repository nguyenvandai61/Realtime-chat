from rest_framework import serializers
from realtime_chat.models import Emotion


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = '__all__'