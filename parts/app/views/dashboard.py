from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from parts.app.partsnumber import models
from parts.app.arrival.models import PartsArrival


class DashboardViewsTemplate(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardViewsTemplate,
                        self).get_context_data(**kwargs)
        context['partsnumber'] = models.PartsNumber.objects.all()
        context['arrival'] = PartsArrival.objects.all().count()
        context['complete'] = PartsArrival.objects.filter(
            remarks__contains='COMPLETED').count()
        context['not_complete'] = PartsArrival.objects.filter(
            remarks__contains='NOT COMPLETED').count()
        context['lacking'] = PartsArrival.objects.filter(
            remarks__contains='LACKING').count()
        return context
