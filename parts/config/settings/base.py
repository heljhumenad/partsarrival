import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Path for building and collecting static files
STATIC_FILES_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    "parts.app.accounts",
    "parts.app.partsnumber",
    "parts.app.advisor",
    "parts.app.arrival",
    "parts.app.views",
    "parts.app.mixins",
    "parts.app.dashboard",
    # Testing app module
    "parts.app.tests",
    # Third partyP
    "bootstrap_modal_forms",
    "rest_framework"
]

MIDDLEWARE = [
    # In built middleware
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "parts.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(STATIC_FILES_PATH, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "parts.config.wsgi.application"

# Database Configurations
DATABASE_HOST = config('DB_HOST')
DATABASE_PASSWORD = config('DB_PASSWORD') 
DATABASE_USER = config('DB_USERNAME') 
DATABASE_NAME = config('DB_NAME') 
DATABASE_PORT = config('DB_PORT') 

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": DATABASE_HOST,
        "PASSWORD": DATABASE_PASSWORD,
        "USER": DATABASE_USER,
        "NAME": DATABASE_NAME,
        "PORT": DATABASE_PORT,
    }
}


# Database Caches
CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'systemcache',
        }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

# Based on the local timezone
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
TIME_ZONE = "Asia/Manila"

USE_I18N = True

USE_L10N = False

USE_TZ = True  # Using aware timezones

DATE_INPUT_FORMATS = ['%m/%d/%Y']

# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_ROOT = os.path.join(STATIC_FILES_PATH, "staticfiles")
STATIC_URL = "/static/"


STATICFILES_DIRS = [
    os.path.join(STATIC_FILES_PATH, "static"),
    # include other static files for development
    ("dev_js", os.path.join(STATIC_FILES_PATH, "static")),
]

# Do not store cookies when browser close
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

