import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("dashboard/", include("parts.app.dashboard.urls")),

    path("", include("parts.app.accounts.urls")),

    path("accounts/", include("django.contrib.auth.urls")),

    path("partsnumber/", include("parts.app.partsnumber.urls")),

    path("advisor/", include("parts.app.advisor.urls")),

    path("arrival/", include("parts.app.arrival.urls")),

    path("__debug__", include(debug_toolbar.urls)),  # Debug purposes

    # Restframework
    path("api-auth/", include("rest_framework.urls")),
]
