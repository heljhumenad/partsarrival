from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from parts.app.advisor.models import ServiceAdvisor
from parts.app.arrival.models import PartsArrival
from parts.app.partsnumber.models import PartsNumber


class DashboardViewsTemplate(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(DashboardViewsTemplate,
                        self).get_context_data(**kwargs)
        # Refactor the queryset
        context['partsnumber'] = PartsNumber.objects.values('id').count()
        context['arrival'] = PartsArrival.objects.values('id').count()
        context['complete'] = PartsArrival.objects.filter(
            remarks__contains='COMPLETED').count()
        context['not_complete'] = PartsArrival.objects.filter(
            remarks__contains='NOT COMPLETED').count()
        context['lacking'] = PartsArrival.objects.filter(
            remarks__contains='LACKING').count()
        context['service_advisor'] = ServiceAdvisor.objects.values('id').count()
        return context
