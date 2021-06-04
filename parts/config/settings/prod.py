from .base import *

DEBUG=False

ALLOWED_HOST = ['parts-arrival.herokuapp.com', '127.0.0.1:8000']

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware',]

