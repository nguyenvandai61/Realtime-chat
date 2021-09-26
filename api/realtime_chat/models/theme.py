from django.db import models
from realtime_chat.models.room import Room


class Theme(models.Model):
    """
    Theme model
    """
    name = models.CharField(max_length=255)
    background = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'
        db_table = 'theme'