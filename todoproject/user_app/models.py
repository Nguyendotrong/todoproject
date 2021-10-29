from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import validators
from .constants import TYPE_GENDER


class User(AbstractUser):

    class Meta:
        ordering = ['id']

    phone_validator = validators.UnicodePhoneValidator

    avatar = CloudinaryField("avatar", null=True)
    gender = models.CharField(max_length=10, choices=TYPE_GENDER, default=0)
    email = models.EmailField(_('email address'), blank=True,unique=True)
    phone = models.CharField(max_length=10, null=True,unique=True,
        help_text=_('Enter a valid phone. This value may contain number, exactly 10 numbers'),
        validators=[phone_validator],
        error_messages={
            'unique': _("A user with that phone already exists."),
        })

    def __str__(self):
        return "username: {}".format(self.username)

    """ Informative name for model """

    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)
