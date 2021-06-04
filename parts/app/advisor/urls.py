from django.urls import path, re_path

from parts.app.views import advisor

app_name = "advisor"

urlpatterns = [
    path("", advisor.AdvisorTemplateView.as_view(), name="advisor_index"),
    path("create", advisor.AdvisorCreateView.as_view(), name="advisor_create"),
    path(
        "update/<int:pk>",
        advisor.AdvisorUpdateView.as_view(),
        name="advisor_update_view",
    ),
    path(
        "show/<int:pk>", advisor.AdvisorDetailView.as_view(), name="advisor_read_view"
    ),
]
