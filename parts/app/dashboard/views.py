from django.shortcuts import render
from django.views.generic import TemplateView

from parts.app.advisor.models import ServiceAdvisor
from parts.app.arrival.models import PartsArrival
from parts.app.partsnumber.models import PartsNumber


class DashboardTemplateView(TemplateView):
    pass
