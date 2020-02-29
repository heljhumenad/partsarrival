from django.urls import path

from parts.app.views import advisor


app_name = "advisor"

urlpatterns = [
    path(
        "dashboard/index",
        advisor.AdvisorTemplateView.as_view(),
        name="advisor_index"
    ),
    path(
        "create/advisor/",
        advisor.AdvisorCreateView.as_view(),
        name="advisor_create"
    ),
    path(
        "update/advisor/<int:pk>/view/",
        advisor.AdvisorUpdateView.as_view(),
        name="advisor_update_view",
    ),
]
