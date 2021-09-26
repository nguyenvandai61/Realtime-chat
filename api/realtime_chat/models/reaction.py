from django.db import models
from .user import User
from .message import Message
from .emotion import Emotion


class Reaction(models.Model):
    """
    Reaction model
    """
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    emotion = models.ForeignKey(Emotion, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reaction'