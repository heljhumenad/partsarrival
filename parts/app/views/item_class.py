#  View Class for Partnumber and its description
from django.url import reverse_lazy
from django.views import generic
from django.utils.translation import ugettext_lazy as _

from parts.app.partsnumber import PartNumberClass


class PartnumberClassTemplateView(generic.TemplateView):
    pass
