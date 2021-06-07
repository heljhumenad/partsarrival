from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from parts.app.advisor.models import ServiceAdvisor


@admin.register(ServiceAdvisor)
class ServiceAdvisorAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = _("Service Advisor Admin")
        verbose_name_plural = _("Services Advisor Admin")
        
    list_display = ['first_name', 'last_name', 'designation']
# Register your models here.
