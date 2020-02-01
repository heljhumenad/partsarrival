from django.views import generic
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from parts.app.partsnumber.models import PartsNumber, UnitMeasure
from parts.app.forms import partsnumber_form 

class PartNumberTemplateView(generic.ListView):
    template_name = 'partsnumber/index.html'
    model = PartNumber
    paginate_by = 2

class PartNumberCreateView(generic.CreateView):
    template_name = 'partsnumber/add_partnumber.html'
    model = PartsNumber
    form_class = partsnumber_form.PartsNumberForm
    success_url = reverse_lazy('partsnumber:parts_number_index_view')

class UnitofMeasureCreateView(generic.CreateView):
     template_name = 'partsnumber/unit_of_measure.html'
     model = UnitMeasure
     form_class = partsnumber_form.UnitofMeasureForm
     success_url = reverse_lazy('partsnumber:parts_number_index_view')
