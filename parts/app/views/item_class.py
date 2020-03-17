#  View Class for Partnumber and its description
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import ugettext_lazy as _

from parts.app.partsnumber.models import PartNumberClass
from parts.app.forms import item_class_form


class PartnumberClassTemplateView(generic.ListView):
    template_name = "item_class/index.html"
    model = PartNumberClass
    paginate_by = 2
    queryset = PartNumberClass.objects.all()


class PartnumberClassCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "item_class/add_class_partnumber.html"
    form_class = item_class_form.PartNumberClassForm
    success_url = reverse_lazy("partsnumber:parts_show_class")

    def get_context_data(self, **kwargs):
        context = super(PartnumberClassCreateView,
                        self).get_context_data(**kwargs)
        context["partnumber_class"] = PartNumberClass.objects.all()
        return context


class PartnumberClassUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "item_class/add_class_partnumber.html"
    form_class = item_class_form.PartNumberClassForm
    success_url = reverse_lazy("partsnumber:parts_show_class")

    def get_object(self, query_pk_and_slug=None):
        item_class = PartNumberClass.objects.filter(
            id=self.kwargs["pk"]).first()
        return item_class


class PartsNumberClassDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "item_class/read_item_class.html"
    model = PartNumberClass
    context_object_name = 'item_class'

    def get_object(self, query_pk_and_slug=None):
        item_class = PartNumberClass.objects.filter(
            id=self.kwargs["pk"]).first()
        return item_class
