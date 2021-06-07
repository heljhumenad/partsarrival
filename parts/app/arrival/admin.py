from django.contrib import admin

from parts.app.arrival.models import PartsArrival


@admin.register(PartsArrival)
class PartsArrivalAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'ro_number',
                    'item_class', 'advisor', 'partnumber',
                    'qty', 'remarks', 'date_arrival'
                    ]
