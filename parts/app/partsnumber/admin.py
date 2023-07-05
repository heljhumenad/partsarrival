from django.contrib import admin
from django.utils.translation import gettext as _

from parts.app.partsnumber.models import SourceCode

# Register your models here.
@admin.register(SourceCode)
class SourceCodeAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = _("Source Code")
        verbose_name_plural = _("Source Codes Description")

    list_display = ['code', 'desc']
