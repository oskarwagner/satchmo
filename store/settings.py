# Django settings for satchmo project.
# This is a recommended base setting for further customization, default for clonesatchmo.py
import os

DIRNAME = os.path.dirname(os.path.normpath(os.path.abspath(__file__)))

DJANGO_PROJECT = 'store'
DJANGO_SETTINGS_MODULE = 'store.settings'

ADMINS = (
     ('Thomas Rega', 'thomas.rega@potstar.biz'),         # tuple (name, email) - important for error reports sending, if DEBUG is disabled.
)

MANAGERS = ADMINS

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Berlin'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 2

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# Image files will be stored off of this path
#
# If you are using Windows, recommend using normalize_path() here
#
# from satchmo_utils.thumbnail import normalize_path
# MEDIA_ROOT = normalize_path(os.path.join(DIRNAME, 'static/'))
MEDIA_ROOT = os.path.join(DIRNAME, 'static/')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = "/media/"

# STATIC_ROOT can be whatever different from other dirs
STATIC_ROOT = os.path.join(DIRNAME, 'static-collect/')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(DIRNAME, 'static/'),
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.doc.XViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "threaded_multihost.middleware.ThreadLocalMiddleware",
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
    #"satchmo_ext.recentlist.middleware.RecentProductMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

#this is used to add additional config variables to each request
# NOTE: If you enable the recent_products context_processor, you MUST have the
# 'satchmo_ext.recentlist' app installed.
TEMPLATE_CONTEXT_PROCESSORS = (
        'satchmo_store.shop.context_processors.settings',
        'django.contrib.auth.context_processors.auth',
        #'satchmo_ext.recentlist.context_processors.recent_products',
        # do not forget following. Maybe not so important currently
        # but will be
        'django.core.context_processors.media',   # MEDIA_URL
        'django.core.context_processors.static',  # STATIC_URL
)

ROOT_URLCONF = 'store.urls'

TEMPLATE_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    #'registration',
    'sorl.thumbnail',
    'keyedcache',
    'livesettings',
    'l10n',
    'satchmo_store.shop',
    'satchmo_store.contact',
    'satchmo_utils.thumbnail',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    #'satchmo_store.contact.supplier',
    #'shipping.modules.tiered',
    #'satchmo_ext.newsletter',
    #'satchmo_ext.recentlist',
    #'testimonials',         # dependency on  http://www.assembla.com/spaces/django-testimonials/
    'product',
    'product.modules.configurable',
    'product.modules.custom',
    #'product.modules.downloadable',
    #'product.modules.subscription',
    #'satchmo_ext.product_feeds',
    #'satchmo_ext.brand',
    'payment',
    'payment.modules.dummy',
    #'payment.modules.purchaseorder',
    #'payment.modules.giftcertificate',
    #'satchmo_ext.wishlist',
    #'satchmo_ext.upsell',
    #'satchmo_ext.productratings',
    #'satchmo_ext.satchmo_toolbar',
    'satchmo_utils',
    #'shipping.modules.tieredquantity',
    #'satchmo_ext.tieredpricing',
    #'typogrify',            # dependency on  http://code.google.com/p/typogrify/
    'debug_toolbar',
    'app_plugins',
    #
    'store.localsite',
)

AUTHENTICATION_BACKENDS = (
    'satchmo_store.accounts.email-auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

#### Satchmo unique variables ####
#from django.conf.urls.defaults import patterns, include
SATCHMO_SETTINGS = {
    'SHOP_BASE': '',
    'MULTISHOP': False,
    #'SHOP_URLS' : patterns('satchmo_store.shop.views',)
}

SKIP_SOUTH_TESTS = True

# Load the local settings
from local_settings import *
