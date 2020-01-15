from .base import *

# Installed Apps
INSTALLED_APPS += [
    'django_extensions',
    'bootstrap4',
    'debug_toolbar',
]

# Customize login accounts
LOGIN_REDIRECT_URL = 'accounts:account_view'
LOGOUT_REDIRECT_URL = 'login'
AUTH_USER_MODEL = 'accounts.CustomUser'

#  Handle debug toolbars internal ip address that link to localhost or 127.0.0.0.1
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1', 'localhost',)
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

# DEBUG Toolbar Settings
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True,

}
