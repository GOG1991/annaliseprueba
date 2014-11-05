"""
Django settings for annalise project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')fryi8_zstx%q82dn9@5so(p-u$g1yly5hi)k!sc7s8q-c#4x7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['super24.com.mx']

# Application definition

INSTALLED_APPS = (
    'suit',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'tinymce',
    'annalise_cms',
    'annalise_job',
    'annalise_investors',
    'disqus',
    'south',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

#Procesadores de contexto globales
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'annalise_cms.contextProcessors.menu',
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'annalise.urls'

WSGI_APPLICATION = 'annalise.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 's24site0907',
        'USER': 'sup24app',
        'PASSWORD':'n3Lkss55',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-Mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTH_PROFILE_MODULE = 'annalise_cms.autor'
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/sup24s/app/static/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')
MEDIA_URL = '/media/'

FILEBROWSER_MEDIA_URL = '/media/'
FILEBROWSER_URL_FILEBROWSER_MEDIA = '/media/filebrowser/'
FILEBROWSER_URL_TINYMCE = "js/tiny_mce/"
FILEBROWSER_PATH_TINYMCE = "js/tiny_mce/"

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'skin':'default', #Copiar el skin a thmes
    'relative_urls': False,
    'theme_advanced_toolbar_location':"top",
}

#Default category
PRODUCTS = 4


#Templates
TEMPLATE_DIRS = [os.path.join(os.path.dirname(__file__) , 'templates'),]
#Disqus credentials
DISQUS_API_KEY = 'KpLVCM5brY9ORPv1A55QlsWTWlSHavuQBM1ErvjgadQ84k1wtE8IeEaJePS4EIWm'
DISQUS_WEBSITE_SHORTNAME = 'super24s'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'super24shy@gmail.com'
EMAIL_HOST_PASSWORD = 'NVwbx7Eie,HC'
EMAIL_PORT = 587

#Personalizar captcha
CAPTCHA_FONT_SIZE = 40

#excluirmenu
EXCLUDEMENU = [3,4]

#Personalizar suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'Annalise',
    'SHOW_REQUIRED_ASTERISK': True,
    'MENU': (
        # Reorder app models
        # Separator
        '-',
        {'app': 'annalise_cms', 'label': 'CMS', 'icon':'icon-book'},
        {'app': 'annalise_investors', 'label': 'Inversionistas', 'icon':'icon-book'},
        {'app': 'annalise_job', 'label': 'Vacantes y aspirantes', 'icon':'icon-book'},
        {'app': 'flatpages', 'label': 'Paginas', 'icon':'icon-book'},

    )
}
