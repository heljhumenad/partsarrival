from django.urls import path
from django.utils.translation import ugettext_lazy as _

from parts.app.views import arrival

app_name = 'arrival'

urlpatterns = [
    path(
        "index/",
        arrival.PartsArrivalTemplateView.as_view(),
        name="arrival_index",
    ),
    path(
        "create-view/",
        arrival.PartsArrivalCreateView.as_view(),
        name="arrival_create"
    ),

]
