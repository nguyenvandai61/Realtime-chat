from django.db import models;

class RoomPrivateMixin(models.Model):
    """
    This is a mixin for private rooms.
    """
    class Meta:
        abstract = True;
    # The room's name.
    name = models.CharField(max_length=50);
    # The room's password.
    password = models.CharField(max_length=50);
    # The room's members.
    members = models.ManyToManyField('User', related_name='rooms');
    # The room's messages.
    messages = models.ManyToManyField('Message', related_name='rooms');

class PublicRoomMixin(models.Model):
    """
    This is a mixin for public rooms.
    """
    class Meta:
        abstract = True;
    # The room's name.
    name = models.CharField(max_length=50);
    # The room's members.
    members = models.ManyToManyField('User', related_name='rooms');
    # The room's messages.
    messages = models.ManyToManyField('Message', related_name='rooms');


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    is_private = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    # The room's owner.
    owner = models.ForeignKey('User', on_delete=models.CASCADE);
    created_at = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255, default='default')
    no_members = models.IntegerField(default=0)
    last_message = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
