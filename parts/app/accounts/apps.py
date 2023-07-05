from django.apps import AppConfig

from parts.config.settings.base import DEFAULT_BASE_PATH


class AccountsConfig(AppConfig):
    name = DEFAULT_BASE_PATH + "accounts"
