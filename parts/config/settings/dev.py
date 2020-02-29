from .base import *
from django.conf import settings

# Installed Apps
INSTALLED_APPS += [
    "django_extensions",
    "bootstrap4",
    "debug_toolbar",
]

# Customize login accounts
LOGIN_REDIRECT_URL = "accounts:account_view"
LOGOUT_REDIRECT_URL = "accounts:login"
AUTH_USER_MODEL = "accounts.CustomUser"

#  Handle debug toolbars internal ip address that link to localhost or 127.0.0.0.1
if DEBUG:
    INTERNAL_IPS = (
        "127.0.0.1",
        "localhost",
    )
    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

# Database Configurations
DATABASE = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": settings.DATABASE_HOST,
        "PASSWORD": settings.DATABASE_PASSWORD,
        "USER": settings.DATABASE_USER,
        "NAME": settings.DATABASE_NAME,
        "PORT": settings.DATABASE_PORT,
    }
}

# DEBUG Toolbar Settings
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": True,
}
