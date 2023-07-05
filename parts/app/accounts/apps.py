from django.apps import AppConfig

from parts.config.settings.base import DEFAULT_BASE_PATH


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = DEFAULT_BASE_PATH + "accounts"
