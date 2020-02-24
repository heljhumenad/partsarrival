from django.views import generic
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from parts.app.partsnumber.models import PartsNumber, UnitMeasure
from parts.app.forms import partsnumber_form 

# PartNumber
class PartNumberTemplateView(generic.ListView):
    template_name = 'partsnumber/index.html'
    model = PartsNumber
    paginate_by = 2

class PartNumberCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'partsnumber/add_partnumber.html'
    model = PartsNumber
    form_class = partsnumber_form.PartsNumberForm
    success_url = reverse_lazy('partsnumber:parts_number_index_view')

    def get_context_data(self, **kwargs):
        context = super(PartNumberCreateView, self).get_context_data(**kwargs)
        context['partsnumber_id'] = PartsNumber.objects.all()
        return context

class PartNumberUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'partsnumber/add_partnumber.html'
    form_class = partsnumber_form.PartsNumberForm
    success_url = reverse_lazy('partsnumber:parts_number_index_view')

    def get_object(self, query_pk_and_slug=None):
        partsnumber = PartsNumber.objects.filter(
            id=self.kwargs['pk']
            ).first()
        return partsnumber

class UnitofMeasureCreateView(generic.CreateView):
     template_name = 'partsnumber/unit_of_measure.html'
     model = UnitMeasure
     form_class = partsnumber_form.UnitofMeasureForm
     success_url = reverse_lazy('partsnumber:parts_number_index_view')
