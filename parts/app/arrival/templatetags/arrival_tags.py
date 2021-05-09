from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def remark_status(remarks):

    NOT_COMPLETED = 'NOT COMPLETED'
    COMPLETED = 'COMPLETED'
    LACKING = 'LACKING'

    # btn size
    xs = 'xs'
    buttons = None

    if remarks == NOT_COMPLETED:
        buttons = '<button class="btn btn-danger btn-{}"><b>{}<b></button>'.format(
            xs, remarks)
        return mark_safe(buttons)
    elif remarks == COMPLETED:
        buttons = '<button class="btn btn-success btn-{}"><b>{}<b></button>'.format(
            xs, remarks)
        return mark_safe(buttons)
    elif remarks == LACKING:
        buttons = '<button class="btn btn-warning btn-{}"><b>{}<b></button>'.format(
            xs, remarks)
        return mark_safe(buttons)
