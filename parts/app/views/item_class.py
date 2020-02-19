#  View Class for Partnumber and its description
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

from parts.app.partsnumber.models import PartNumberClass
from parts.app.forms import item_class_form


class PartnumberClassTemplateView(generic.TemplateView):
    pass


class PartnumberClassCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'item_class/add_class_partnumber.html'
    form_class = item_class_form.PartNumberClassForm
    success_url = reverse_lazy('partsnumber:parts_number_index_view')


class PartnumberClassUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'item_class/update_class_partnumber.html'
    form_class = item_class_form.PartNumberClassForm
    success_url = reverse_lazy('partsnumber:parts_number_index_view')

    def get_object(self, query_pk_and_slug):
        item_class = PartNumberClass.object.filter(
            id = self.kwargs['pk']).first()
        return item_class
    
