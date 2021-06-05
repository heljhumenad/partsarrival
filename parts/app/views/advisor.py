from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from parts.app.advisor.models import ServiceAdvisor
from parts.app.mixins.common_mixins import ServiceAdvisorMixins
from parts.core.forms import AdvisorForm


class AdvisorTemplateView(ServiceAdvisorMixins, generic.ListView):
    template_name = "advisor/index.html"
    model = ServiceAdvisor
    queryset = ServiceAdvisor.objects.all()
    paginate_by = 2
    # context_object_name = "advisor"


class AdvisorCreateView(ServiceAdvisorMixins, generic.CreateView):
    template_name = "advisor/add_advisor.html"
    form_class = AdvisorForm
    messages = 'added'
    success_url = reverse_lazy("advisor:advisor_index")

    def get_context_data(self, **kwargs):
        context = super(AdvisorCreateView, self).get_context_data(**kwargs)
        context["advisor"] = ServiceAdvisor.objects.all()
        return context


class AdvisorUpdateView(ServiceAdvisorMixins, generic.UpdateView):
    template_name = "advisor/add_advisor.html"
    form_class = AdvisorForm
    model = ServiceAdvisor
    messages = 'updated'
    success_url = reverse_lazy("advisor:advisor_index")

    def get_object(self):
        return super(AdvisorUpdateView, self).get_object()


class AdvisorDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "advisor/read_advisor.html"
    model = ServiceAdvisor
    context_object_name = "advisor"

    def get_object(self, query_pk_and_slug=None):
        advisor = ServiceAdvisor.objects.all().filter(
                id=self.kwargs["pk"]).first()
        return advisor
