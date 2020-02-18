from django.urls import path
from parts.app.views import partsnumber
from parts.app.views import item_class

app_name = 'partsnumber'

urlpatterns = [

    path('dashboard/index',
         partsnumber.PartNumberTemplateView.as_view(),
         name='parts_number_index_view'
         ),

    path('dashboard/add/partnumber',
         partsnumber.PartNumberCreateView.as_view(),
         name='parts_number_create_view'
         ),

    path('dashboard/add/um',
         partsnumber.UnitofMeasureCreateView.as_view(),
         name='parts_um_create_view'
         ),

    path('dashboard/show/partnumberclass/',
         item_class.PartnumberClassTemplateView.as_view(),
         name='parts_show_class'
         )

]