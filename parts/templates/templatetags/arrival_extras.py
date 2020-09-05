# !/usr/bin/python3
from django import template

register = template.Library()


@register.simple_tag
def remark_status(remarks):

    NOT_COMPLETED = 'NOT COMPLETED'
    COMPLETED = 'COMPLETED'
    LACKING = 'LACKING'

    # btn size
    xs = 'xs'

    if remarks == NOT_COMPLETED:
        return '<a href='' class="btn btn-danger btn-{}"><b>{}<b></a>'.format(
            xs, remarks)
    elif remarks == COMPLETED:
        return '<a href='' class="btn btn-success btn-{}"><b>{}<b></a>'.format(
            xs, remarks)
    elif remarks == LACKING:
        '<a href='' class="btn btn-danger btn-{}"><b>{}<b></a>'.format(
            xs, remarks)
