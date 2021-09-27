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

class RoomThemeMixin(models.Model):
    theme = models.ForeignKey('Theme', on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True;

class Room(RoomThemeMixin):
    id = models.AutoField(primary_key=True)
    is_private = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    # The room's owner.
    owner = models.ForeignKey('User', on_delete=models.CASCADE);
    created_at = models.DateTimeField(auto_now_add=True)
    no_members = models.IntegerField(default=1)
    last_message = models.ForeignKey('Message', related_name="last_message", on_delete=models.CASCADE, null=True, blank=True)
    messages = models.ManyToManyField('Message', related_name='rooms')

    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    class Meta:
        db_table = 'room'


