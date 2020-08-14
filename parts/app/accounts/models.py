from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


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
