from django.urls import path

from parts.app.views import accounts

app_name = "accounts"

urlpatterns = [
    path("dashboard", accounts.AccountTemplateView.as_view(), name="account_view"),
    path("", accounts.AccountLoginView.as_view(), name="login"),
    path("logout", accounts.AccountLogoutView.as_view(), name="logout_view"),
    path("update/user/<int:pk>", accounts.AccountEditView.as_view(), name="edit_user"),
    path(
        "changepassword/user/<int:pk>",
        accounts.AccountChangePasswordView.as_view(),
        name="changepassword",
    ),
]
