from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from parts.app.advisor.models import ServiceAdvisor
from parts.app.forms.advisor_forms import AdvisorForm


class AdvisorTemplateView(generic.ListView):
    template_name = "advisor/index.html"
    model = ServiceAdvisor
    paginate_by = 2


class AdvisorCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "advisor/add_advisor.html"
    form_class = AdvisorForm
    success_url = reverse_lazy("advisor:advisor_index")

    def get_context_data(self, **kwargs):
        context = super(AdvisorCreateView, self).get_context_data(**kwargs)
        context["advisor"] = ServiceAdvisor.objects.all()
        return context


class AdvisorUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "advisor/add_advisor.html"
    form_class = AdvisorForm
    success_url = reverse_lazy("advisor:advisor_index")

    def get_object(self, query_pk_and_slug=None):
        advisor = ServiceAdvisor.objects.all().filter(
            id=self.kwargs["pk"],).first()
        return advisor


class AdvisorDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "advisor/read_advisor.html"
    model = ServiceAdvisor
    context_object_name = 'advisor'

    def get_object(self, query_pk_and_slug=None):
        advisor = ServiceAdvisor.objects.all().filter(
            id=self.kwargs['pk']
        ).first()
        return advisor
