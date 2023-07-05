from django.apps import AppConfig
from parts.config.settings.base import DEFAULT_BASE_PATH


class DashboardConfig(AppConfig):
    name = DEFAULT_BASE_PATH + 'dashboard'
