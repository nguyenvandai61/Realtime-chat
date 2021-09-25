from django.contrib.auth.models import User as DjangoUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserActiveMixin(models.Model):
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    last_active = models.DateTimeField(
        _('last active'),
        auto_now=True,
        help_text=_('The last time the user was active.'),
    )

    class Meta:
        abstract = True


class UserDetailMixin(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    

class User(DjangoUser, UserActiveMixin, UserDetailMixin):
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'auth_user'
