from django.views import generic
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from parts.app.mixins.common_mixins import PartsNumberMixin
from parts.app.partsnumber.models import PartsNumber, UnitMeasure
from parts.app.forms import partsnumber_form


class PartNumberTemplateView(generic.ListView):
    template_name = "partsnumber/index.html"
    model = PartsNumber
    paginate_by = 10
    context_object_name = "partsnumber"


class PartNumberCreateView(PartsNumberMixin, generic.CreateView):
    template_name = "partsnumber/add_partnumber.html"
    model = PartsNumber
    form_class = partsnumber_form.PartsNumberForm
    messages = "added"
    success_url = reverse_lazy("partsnumber:parts_number_create_view")

    def get_context_data(self, **kwargs):
        context = super(PartNumberCreateView, self).get_context_data(**kwargs)
        context["partsnumber_id"] = PartsNumber.objects.all()
        return context
    
    
class PartsNumberDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "partsnumber/read_partnumber.html"
    model = PartsNumber
    context_object_name = "partsnumber"

    def get_object(self):
        return super(PartsNumberDetailView, self).get_object()


class PartNumberUpdateView(PartsNumberMixin, generic.UpdateView):
    template_name = "partsnumber/add_partnumber.html"
    form_class = partsnumber_form.PartsNumberForm
    success_url = reverse_lazy("partsnumber:parts_number_index_view")
    model = PartsNumber
    messages = "updated"
    context_object_name = "partsnumber"

    def get_object(self):
        return super(PartNumberUpdateView, self).get_object()


class PartnumberDeleteView(PartsNumberMixin, generic.DeleteView):
    template_name = "partsnumber/confirm_delete.html"
    success_url = reverse_lazy("partsnumber:parts_number_index_view")
    model = PartsNumber
    context_object_name = "partsnumber"

    def get_object(self):
        return super(PartnumberDeleteView, self).get_object()


class SearchView(LoginRequiredMixin, generic.ListView):
    template_name = "partsnumber/search_results.html"
    model = PartsNumber

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = PartsNumber.objects.filter(
            Q(partnumber__icontains=query) | Q(description__icontains=query)
        )
        return object_list


class UnitofMeasureCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "partsnumber/unit_of_measure.html"
    model = UnitMeasure
    form_class = partsnumber_form.UnitofMeasureForm
    success_url = reverse_lazy("partsnumber:parts_um_create_view")
