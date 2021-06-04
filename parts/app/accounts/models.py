from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from parts.core.models import TimeStampModel


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()

    @property
    def get_user_account_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def get_user_email(self):
        return self.email


class ProfileUser(TimeStampModel, models.Model):

    USER_LEVEL_ROLE = (
        (1, "Manager"),
        (2, "Partsman"),
        (3, "Insurance Officer"),
        (4, "Supervisor"),
        (5, "Administrator"),
    )
    role = models.PositiveSmallIntegerField(
        verbose_name=_("User Role Level"),
        choices=USER_LEVEL_ROLE
    )
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{0} {1}".format(self.user, self.role)
