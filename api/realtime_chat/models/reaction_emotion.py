from django.db import models


class ReactionEmotion(models.Model):
    """
    ReactionEmotion model
    """
    reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
