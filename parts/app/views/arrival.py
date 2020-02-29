from django.views import generic
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin

from parts.app.arrival.models import PartsArrival
from parts.app.forms.arrival_form import PartsArrivalForm


class PartsArrivalTemplateView(LoginRequiredMixin, generic.TemplateView):
    pass


class PartsArrivalCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'arrival/add_arrival.html'
    form_class = PartsArrivalForm
    success_url = reverse_lazy('arrival:arrival_index')

    # def get_context_data(self,  **kwargs):
    #     context = super(PartsArrivalCreateView,
    #                     self).get_context_data(**kwargs)
    #     context['arrival'] = PartsArrival.objects.all()
    #     return context
