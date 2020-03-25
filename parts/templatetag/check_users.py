# !/usr/bin/python3
from django import template

register = template.Library()


def check_user_is_staff(self, request):

    # tag to check if user has credentials to login
    # and view certain template

    pass
