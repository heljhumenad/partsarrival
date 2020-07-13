# !/usr/bin/python3
from django import template

register = template.Library()


def check_user_is_staff():

    # tag to check if user has credentials to login
    # and view certain template

    pass


@register.tag
def remark_status(status):
    if status == 'LACKING':
        return "<button class='btn btn-warning btn-xs'>{}</button>".format(status)
    elif status == 'COMPLETED':
        return " <button class='btn btn-warning btn-xs'>{}</button>".format(status)
    elif status == 'NOT COMPLETED':
        return "<button class = 'btn btn-warning btn-xs' >{}< /button >".format(status)
    return status
