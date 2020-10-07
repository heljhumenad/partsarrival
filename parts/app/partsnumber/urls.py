from django.urls import path
from parts.app.views import partsnumber
from parts.app.views import item_class

app_name = "partsnumber"

urlpatterns = [
    path(
        "index",
        partsnumber.PartNumberTemplateView.as_view(),
        name="parts_number_index_view",
    ),
    path(
        "add/partnumber",
        partsnumber.PartNumberCreateView.as_view(),
        name="parts_number_create_view",
    ),
    path(
        "update/<int:pk>/partnumbers",
        partsnumber.PartNumberUpdateView.as_view(),
        name="parts_number_update_view",
    ),
    path(
        "read/<int:pk>/",
        partsnumber.PartsNumberDetailView.as_view(),
        name="parts_number_read_view",
    ),
    path(
        "delete/<int:pk>/",
        partsnumber.PartnumberDeleteView.as_view(),
        name="parts_number_delete_view",
    ),
    path(
        "search",
        partsnumber.SearchView.as_view(),
        name="search_query"
    ),
    path(
        "add/um",
        partsnumber.UnitofMeasureCreateView.as_view(),
        name="parts_um_create_view",
    ),
    path(
        "show/partnumberclass/",
        item_class.PartnumberClassTemplateView.as_view(),
        name="parts_show_class",
    ),
    path(
        "add/class/",
        item_class.PartnumberClassCreateView.as_view(),
        name="part_class_create_view",
    ),
    path(
        "update/<int:pk>/class/",
        item_class.PartnumberClassUpdateView.as_view(),
        name="part_class_update_view",
    ),

    path(
        "read/<int:pk>/class/",
        item_class.PartsNumberClassDetailView.as_view(),
        name="item_class_read",
    )
]
