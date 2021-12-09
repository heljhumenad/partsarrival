#  View Class for Partnumber and its description
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from parts.app.partsnumber.models import PartNumberClass
from parts.core.forms import PartNumberClassForm


class PartnumberClassTemplateView(generic.ListView):
    template_name = "item_class/index.html"
    model = PartNumberClass
    paginate_by = 2
    queryset = PartNumberClass.objects.all()


class PartnumberClassCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "item_class/add_class_partnumber.html"
    form_class = PartNumberClassForm
    success_url = reverse_lazy("partsnumber:parts_show_class")

    def get_context_data(self, **kwargs):
        context = super(PartnumberClassCreateView,
                        self).get_context_data(**kwargs)
        context["partnumber_class"] = PartNumberClass.objects.all()
        return context


class PartnumberClassUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "item_class/add_class_partnumber.html"
    form_class = PartNumberClassForm
    model = PartNumberClass
    success_url = reverse_lazy("partsnumber:parts_show_class")
    context_object_name = 'item_class'

    def get_first_object(self):
        return super(PartnumberClassUpdateView, self).get_first_object()


class PartsNumberClassDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "item_class/read_item_class.html"
    model = PartNumberClass
    context_object_name = 'item_class'

    def get_first_object(self):
        return super(PartnumberClassUpdateView, self).get_first_object()
