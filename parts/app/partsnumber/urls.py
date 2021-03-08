from django.urls import path, include

from parts.app import partsnumber, item_class

app_name = "partsnumber"

urlpatterns = [
    # Parts Pattern
    path(
        "", partsnumber.PartNumberTemplateView.as_view(), name="parts_number_index_view"
    ),
    path(
        "create",
        partsnumber.PartNumberCreateView.as_view(),
        name="parts_number_create_view",
    ),
    path(
        "update/<int:pk>",
        partsnumber.PartNumberUpdateView.as_view(),
        name="parts_number_update_view",
    ),
    path(
        "show/<int:pk>",
        partsnumber.PartsNumberDetailView.as_view(),
        name="parts_number_read_view",
    ),
    path(
        "delete/<int:pk>",
        partsnumber.PartnumberDeleteView.as_view(),
        name="parts_number_delete_view",
    ),
    # Unit of Measure Pattern
    path(
        "create/um",
        partsnumber.UnitofMeasureCreateView.as_view(),
        name="parts_um_create_view",
    ),
    # Item Class Pattern
    path(
        "list",
        item_class.PartnumberClassTemplateView.as_view(),
        name="parts_show_class",
    ),
    path(
        "create/class",
        item_class.PartnumberClassCreateView.as_view(),
        name="part_class_create_view",
    ),
    path(
        "update/<int:pk>/class",
        item_class.PartnumberClassUpdateView.as_view(),
        name="part_class_update_view",
    ),
    path(
        "read/<int:pk>/class",
        item_class.PartsNumberClassDetailView.as_view(),
        name="item_class_read",
    ),
    path("search", partsnumber.SearchView.as_view(), name="search_query"),
]
