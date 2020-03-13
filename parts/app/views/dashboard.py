from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from parts.app.partsnumber import models


class DashboardViewsTemplate(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardViewsTemplate,
                        self).get_context_data(**kwargs)
        context['partsnumber'] = models.PartsNumber.objects.all()
        return context
