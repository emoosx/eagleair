import dj_database_url
from base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config(default='postgres://localhost:5432/eagleairdb')
}

INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions'
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True
}

SASS_PROCESSOR_ENABLED = True
