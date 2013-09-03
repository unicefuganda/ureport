#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
# encoding=utf-8


# -------------------------------------------------------------------- #
#                          PATH CONFIGURATION                          #
# -------------------------------------------------------------------- #

import sys, os


filedir = os.path.dirname(__file__)
sys.path.append(os.path.join(filedir))
sys.path.append(os.path.join(filedir, 'rapidsms', 'lib'))
sys.path.append(os.path.join(filedir, 'rapidsms_auth'))
sys.path.append(os.path.join(filedir, 'rapidsms_contact'))
sys.path.append(os.path.join(filedir, 'rapidsms_cvs'))
sys.path.append(os.path.join(filedir, 'rapidsms_generic'))
sys.path.append(os.path.join(filedir, 'rapidsms_geoserver'))
sys.path.append(os.path.join(filedir, 'rapidsms_httprouter_src'))
sys.path.append(os.path.join(filedir, 'rapidsms_polls'))
sys.path.append(os.path.join(filedir, 'rapidsms_script'))
sys.path.append(os.path.join(filedir, 'rapidsms_uregister'))
sys.path.append(os.path.join(filedir, 'rapidsms_ureport'))
sys.path.append(os.path.join(filedir, 'rapidsms_uganda_common'))
sys.path.append(os.path.join(filedir, 'rapidsms_unregister'))
sys.path.append(os.path.join(filedir, 'rapidsms_xforms_src'))
sys.path.append(os.path.join(filedir, 'rapidsms_tracking'))
sys.path.append(os.path.join(filedir, 'django_eav'))
sys.path.append(os.path.join(filedir, 'rapidsms_uganda_ussd'))
sys.path.append(os.path.join(filedir, 'rapidsms_message_classifier'))

sys.path.append(os.path.join(filedir, 'qos_monitor'))


# -------------------------------------------------------------------- #
#                          MAIN CONFIGURATION                          #
# -------------------------------------------------------------------- #
BAD_WORDS = ['poop', ] #list of profanities
TIME_ZONE = "Africa/Kampala"
EMAIL_HOST_USER = ''
EMAIL_HOST = '127.0.0.1'
OPT_IN_WORDS = ['join']
OPT_IN_WORDS_LUO=["donyo","dony","donyo","doyo",]
OPT_IN_CONFIRMATION = "Welcome to UReport! Ureport is a community of Ugandan youth that are dedicated to working for positive change in their communities. Stay tuned for more info."
OPT_OUT_WORDS = ['stop', 'unjoin', 'quit','giki']
OPT_OUT_CONFIRMATION = "Your UReport opt out is confirmed.If you made a mistake,or you want your voice to be heard again,text in JOIN and send it to 8500!All SMS messages are free"

# map bounding box
MIN_LON = '29.55322265625'
MAX_LON = '33.92578125'
MIN_LAT = '-1.0326589311777759'
MAX_LAT = '4.280680030820496'
# map categorized color pallete
CATEGORY_COLORS = ['#AA4643', '#4572A7', '#89A54E', '#80699B', '#3D96AE', '#DB843D', '#92A8CD', '#A47D7C', '#B5CA92']

ADMINS = (
)

gettext = lambda s: s

LANGUAGES = (
    ('ach', gettext('luo')),
    ('en', gettext('English')),
)

# you should configure your database here before doing any real work.
# see: http://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ureport',
        'HOST': 'dbserver',
        'USER': 'postgres',
    }
}

# the rapidsms backend configuration is designed to resemble django's
# database configuration, as a nested dict of (name, configuration).
#
# the ENGINE option specifies the module of the backend; the most common
# backend types (for a GSM modem or an SMPP server) are bundled with
# rapidsms, but you may choose to write your own.
#
# all other options are passed to the Backend when it is instantiated,
# to configure it. see the documentation in those modules for a list of
# the valid options for each.
INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.bucket",
    },
}


# to help you get started quickly, many django/rapidsms apps are enabled
# by default. you may wish to remove some and/or add your own.
INSTALLED_APPS = [
    "ureport",
    "djtables",
    "mptt",
    "uni_form",
    "django_extensions",
    "rapidsms.contrib.handlers",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.humanize",

    # the rapidsms contrib apps.
    "rapidsms.contrib.default",
    "rapidsms.contrib.locations",
    "rapidsms.contrib.locations.nested",
    "geoserver",
    "rapidsms.contrib.messaging",
    "rapidsms.contrib.registration",
    "eav",
    "auth",
    "rapidsms_httprouter",
    "poll",
    "generic",
    "contact",
    "script",
    "unregister",
    "tracking",
    "uganda_common",
    "rapidsms",
    "rapidsms_xforms",
    "ussd",
    "monitor",
    "message_classifier",
    "celery",
    "djcelery",
    #"permission",
   # nothing after south
    "south",
    "django_nose" #Except nose must come after south so that it runs migrations properly!!
]

SMS_APPS = [
    "monitor",
    "ureport",
    "script",
    "poll",
    "unregister",
    #"rapidsms_xforms",
]


# this rapidsms-specific setting defines which views are linked by the
# tabbed navigation. when adding an app to INSTALLED_APPS, you may wish
# to add it here, also, to expose it in the rapidsms ui.
RAPIDSMS_TABS = [
     ("rapidsms-dashboard", "Home"),
     ("ureport-about", "About"),
     ("polls-summary", "Polls"),
     ("ureport-stories", "Stories"),
]

AUTHENTICATED_TABS = [
    ("ureport-polls", "Poll Admin"),
    ("messagelog", "Message Log"),
    ("ureport-contact", "uReporters"),
     ("flaggedmessages", "Flagged Messages"),
]

# -------------------------------------------------------------------- #
#                         BORING CONFIGURATION                         #
# -------------------------------------------------------------------- #


# debug mode is turned on as default, since rapidsms is under heavy
# development at the moment, and full stack traces are very useful
# when reporting bugs. don't forget to turn this off in production.
DEBUG = TEMPLATE_DEBUG = True

# after login (which is handled by django.contrib.auth), redirect to the
# dashboard rather than 'accounts/profile' (the default).
LOGIN_REDIRECT_URL = "/"


# use django-nose to run tests. rapidsms contains lots of packages and
# modules which django does not find automatically, and importing them
# all manually is tiresome and error-prone.
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
#TEST_RUNNER = "testrunner.NoDbNoseTestSuiteRunner"


# for some reason this setting is blank in django's global_settings.py,
# but it is needed for static assets to be linkable.
MEDIA_URL = "/static/"
ADMIN_MEDIA_PREFIX = "/static/media/"
# this is required for the django.contrib.sites tests to run, but also
# not included in global_settings.py, and is almost always ``1``.
# see: http://docs.djangoproject.com/en/dev/ref/contrib/sites/
SITE_ID = 1

# this is used for geoserver to tell which website this viz should be for (and prevents clashing of
# polls across different websites with the same id
DEPLOYMENT_ID = 1

#model containing blacklisted contacts
BLACKLIST_MODEL= "unregister.Blacklist"

# these weird dependencies should be handled by their respective apps,
# but they're not, so here they are. most of them are for django admin.
TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "generic.context_processors.map_params",
    "uganda_common.context_processors.authtabs",
    "ureport.context_processors.voices",
]

MIDDLEWARE_CLASSES = (
    'ureport.middleware.access_log.UreportAccessLogMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    #'tracking.middleware.UserTrackingMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # "ureport.middleware.permissions.RequirePermissionMiddleware",
     "uganda_common.middleware.accessmiddleware.accessmiddleware.AccessMiddleWare"
)

# -------------------------------------------------------------------- #
#                           HERE BE DRAGONS!                           #
#        these settings are pure hackery, and will go away soon        #
# -------------------------------------------------------------------- #

# these apps should not be started by rapidsms in your tests, however,
# the models and bootstrap will still be available through django.
TEST_EXCLUDED_APPS = [
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rapidsms",
    "rapidsms.contrib.ajax",
    "rapidsms.contrib.httptester",
]


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

# the project-level url patterns
ROOT_URLCONF = "urls"

#caching stuff
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 6000,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 2 * 60 * 60
CACHE_MIDDLEWARE_KEY_PREFIX = ''

ALLOWED = (
    r'/accounts/login(.*)$',
    r'/accounts/logout(.*)$',
    r'/static/(.*)$',
    r'^/$',
    r'/about/$',
    r'/signup/$',
    r'^/bestviz(.*)'

    )

#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
#    'permission.backends.RoleBackend',
#    'permission.backends.PermissionBackend',
#    )

USE_I18N = True
INITIAL_USSD_SCREEN='ussd_root'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

SHOW_CONTACT_INFO = False

USE_NEW_START_POLL = False
ADMIN_UNREGISTER = False

## Testing settings:
## http://hustoknow.blogspot.com/2011/02/setting-up-django-nose-on-hudson.html
# https://nose.readthedocs.org/en/latest/plugins/cover.html
# this is supposed to exclude a dir '--exclude-dir=',
NOSE_ARGS = ('--with-xunit', '--xunit-file=target/reports/unit-test/nosetests.ureport.xml',
	     '--with-coverage', '--cover-html', '--cover-html-dir=target/reports/unit-test/coverage', '--cover-package=poll,uganda_common,unregister,message_classifier,contact,rapidsms_httprouter,rapidsms_ureport',
             '--verbosity=2')

MAP_BOUNDS = {'bottom_left': {'lon': 3292022.5, 'lat': -164636.828},

              'top_right': {'lon': 3896216.5, 'lat': 471764.844}
              }

#MAP_BOUNDS SHOULD MOVE INTO HERE (BEFORE GEOSERVER IS KILLED)
MAP_ARGS = {'center': {'longitude': 33.0, 'latitude': 0.0},
            'scale': 36000
            }

# since we might hit the database from any thread during testing, the
# in-memory sqlite database isn't sufficient. it spawns a separate
# virtual database for each thread, and syncdb is only called for the
# first. this leads to confusing "no such table" errors. We create
# a named temporary instance instead.
import os
import tempfile
import sys

PAGINATION_LIMIT = None

try:
    if os.environ.has_key('LOCAL_SETTINGS'):
        # the LOCAL_SETTINGS environment variable is used by the build server
        sys.path.insert(0, os.path.dirname(os.environ['LOCAL_SETTINGS']))
        from settings_test import *
    else:
        from localsettings import *
except ImportError:
    pass
# if 'test' in sys.argv:
#     DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}


