from django.urls import path
from parts.app.views import partsnumber

app_name = 'partsnumber'

urlpatterns = [

        path('dashboard/',
            partsnumber.PartNumberTemplateView.as_view(),
            name='parts_number_index_view'
            ),

        path('dashboard/add/partnumber',
            partsnumber.PartNumberCreateView.as_view(),
            name='parts_number_create_view'
            ),

]
