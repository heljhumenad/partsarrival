from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager

from parts.models.timestamp import TimeStampModel
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

    USER_LEVEL = (
        ("1", "Manager"),
        ("2", "Partsman"),
        ("3", "Warehouseman")
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    user_level = models.CharField(max_length=200, verbose_name=_("User Level"), choices=USER_LEVEL)

    def __str__(self):
        return "{0} {1}".format(self.user, self.user_level)