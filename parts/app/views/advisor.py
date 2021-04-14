from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import renderers
from rest_framework import generics

from parts.app.advisor.serializers import ServiceAdvisorSerializers
from parts.app.advisor.models import ServiceAdvisor
from parts.app.forms.advisor_forms import AdvisorForm


class AdvisorTemplateView(generics.RetrieveAPIView):
    renderer_classes = [renderers.JSONRenderer]
    serializer_class = ServiceAdvisorSerializers
    queryset = ServiceAdvisor.objects.all()
#    paginate_by = 2
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'advisor': self.object}, template_name="advisor/index.html")


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
    model = ServiceAdvisor
    success_url = reverse_lazy("advisor:advisor_index")

    def get_object(self):
        return super(AdvisorUpdateView, self).get_object()


class AdvisorDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "advisor/read_advisor.html"
    model = ServiceAdvisor
    context_object_name = "advisor"

    def get_object(self, query_pk_and_slug=None):
        advisor = ServiceAdvisor.objects.all().filter(id=self.kwargs["pk"]).first()
        return advisor
