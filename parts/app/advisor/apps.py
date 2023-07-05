from django.apps import AppConfig

from parts.config.settings.base import DEFAULT_BASE_PATH

class AdvisorConfig(AppConfig):
    name = DEFAULT_BASE_PATH + "advisor"
