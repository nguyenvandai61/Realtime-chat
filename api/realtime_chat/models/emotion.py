from django.db import models


class Emotion(models.Model):
    """
    Emotion model
    """
    emotion = models.CharField(max_length=50)
    icon = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'emotion'