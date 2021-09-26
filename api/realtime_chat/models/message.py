from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING


class Message(models.Model):
    content = models.CharField(max_length=200)
    sender = models.ForeignKey('User', on_delete=DO_NOTHING)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    edited_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    replied_to = models.ForeignKey('self', related_name='replied_message', on_delete=DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.message
    
    class Meta:
        db_table='message'
        ordering = ['-timestamp']
    