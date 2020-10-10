from django.urls import path, include


from parts.app.views.home import HomeTemplateView
from parts.app.views.accounts import AccountLoginView

app_name = "home"

urlpatterns = [
    path("", AccountLoginView.as_view(), name="home_template_view"),
]
