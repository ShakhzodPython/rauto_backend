from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from .utils import validate_phone_number


# Create your models here.

class Profile(AbstractUser):
    username = models.CharField(verbose_name=_('username'), max_length=100, unique=True, blank=False, null=False)
    first_name = models.CharField(verbose_name=_("first name"), max_length=150)
    last_name = models.CharField(verbose_name=_("last name"), max_length=150)
    email = models.EmailField(verbose_name=_("email address"), unique=True, blank=True)
    phone_number = models.CharField(verbose_name=_('phone number'), max_length=13, blank=False, null=False,
                                    validators=[validate_phone_number])

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return self.username
