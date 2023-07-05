from django.apps import AppConfig

from parts.config.settings.base import DEFAULT_BASE_PATH


class ArrivalConfig(AppConfig):
    name = DEFAULT_BASE_PATH + "arrival"
