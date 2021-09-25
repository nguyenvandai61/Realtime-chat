from django.db import models
from django.db.models.deletion import DO_NOTHING


class Message(models.Model):
    message = models.CharField(max_length=200)
    sender = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_edited = models.BooleanField(default=False)
    edited_message = models.CharField(max_length=200, default=None, null=True)
    edited_timestamp = models.DateTimeField(auto_now_add=True, default=None, null=True)
    replied_to = models.ForeignKey('self', on_delete=DO_NOTHING, null=True, blank=True)
    reaction_emotions = models.CharField(max_length=200, default=None, null=True)

    def __str__(self):
        return self.message
    
    class Meta:
        db_table='message'
        ordering = ['-timestamp']
    