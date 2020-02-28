from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from parts.app.advisor.models import ServiceAdvisor
from parts.app.forms.advisor_forms import AdvisorForm

class AdvisorTemplateView(generic.TemplateView):
    pass

class AdvisorCreateView(LoginRequiredMixins, generic.CreateView):
    template_name='advisor/add_advisor.html'
