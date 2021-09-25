from django.db import models
from .user import User
from .message import Message


class Reaction(models.Model):
    """
    Reaction model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reaction'