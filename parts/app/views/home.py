from django.urls import reverse_lazy
from django.views import generic


class HomeTemplateView(generic.TemplateView):
    template_name = 'home/index.html'