import dj_database_url
import os

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)

SECRET_KEY = '5nn1-c3=77+kq6k7q9mzt8q51(2x)n$771mu+iueeq1(z7i034'

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': dj_database_url.config()
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'HTTPS')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIR = (
    os.path.join(PROJECT_ROOT, 'static'),
    'sass_processor.finders.CssFinder'
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'eagleair.urls'
WSGI_APPLICATION = 'eagleair.wsgi.application'

BOWER_COMPONENTS_ROOT = os.path.join(PROJECT_ROOT, 'components')

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
LOCAL_APPS = (
    'eagleair',
    'flight',
    'reservation',
    'website',
)
THIRD_PARTY_APPS = (
    'materialize',
    'djangobower',
    'sass_processor',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

BOWER_INSTALLED_APPS = (
    'jquery',
)

SASS_PROCESSOR_ENABLED = False
SASS_PROCESSOR_ROOT = (
    os.path.join(PROJECT_ROOT, 'static')
)

LOGIN_URL = 'django.contrib.auth.views.login'
LOGIN_REDIRECT_URL = '/'
