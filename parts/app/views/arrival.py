from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from parts.app.arrival.models import PartsArrival
from parts.app.mixins.common_mixins import PartsArrivalMixins
from parts.core.forms import PartsArrivalForm


class PartsArrivalListView(PartsArrivalMixins, generic.ListView):
    template_name = "arrival/index.html"
    model = PartsArrival
    paginate_by = 3


class PartsArrivalCreateView(PartsArrivalMixins, generic.CreateView):
    template_name = "arrival/add_arrival.html"
    form_class = PartsArrivalForm
    success_url = reverse_lazy("arrival:arrival_create")
    messages = "added"

    def get_context_data(self, **kwargs):
        context = super(PartsArrivalCreateView, self).get_context_data(
                **kwargs)
        context["arrival"] = PartsArrival.objects.all()
        return context


class PartsArrivalUpdateView(PartsArrivalMixins, generic.UpdateView):
    template_name = "arrival/add_arrival.html"
    form_class = PartsArrivalForm
    success_url = reverse_lazy("arrival:arrival_index")
    messages = "updated"

    def get_object(self, query_pk_and_slug=None):
        query = PartsArrival.objects.filter(id=self.kwargs["pk"]).first()
        return query


class PartsArrivalDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "arrival/read_view.html"
    model = PartsArrival
    context_object_name = "arrival"

    def get_object(self, query_pk_and_slug=None):
        query = PartsArrival.objects.filter(id=self.kwargs["pk"]).first()
        return query
