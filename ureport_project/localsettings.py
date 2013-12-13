# -*- coding: utf-8 -*-

ADMIN_UNREGISTER = True
IBM_TABLES_MANAGED = True
USE_NEW_START_POLL = False
INTERNAL_IPS = ('127.0.0.1')
DBS_TO_IGNORE = ['geoserver']

# -------------------------------------------------------------------- #
#                          PATH CONFIGURATION                          #
# -------------------------------------------------------------------- #
STATIC_URL="/static/media/"
STATIC_ROOT=''
GEOSERVER_URL="/geoserver/"

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
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)-15s %(levelname)-8s [%(module)-20s] %(message)s'
        },
     },
    'handlers': {
        'command': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/uwsgi/app/command.log',
            'formatter' : 'simple'
        },
        'console':{
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'application_log_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/ureport/ureport_application.log',
            'formatter': 'simple',
            'backupCount': 50,
            'maxBytes': 2 ** 20,
        },
        'application_access_log_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/ureport/ureport_access.log',
            'formatter': 'simple',
            'backupCount': 50,
            'maxBytes': 2 ** 20,
        },
     },
    'loggers': {

        'django' : {
            'handlers': ['application_log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'app/ureport' : {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,

        },
        'django.middleware': {
            'handlers': ['application_log_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['application_log_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['application_log_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'ureport.app': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'ureport.tasks': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'ureport.views.poll_views': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'ureport.middleware.access_log': {
            'handlers': ['application_access_log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'poll.app': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'poll.models': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rapidsms_httprouter.models': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rapidsms_httprouter.views': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rapidsms_httprouter.router': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    	'script.utils.outgoing' :{
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
	'script.managers' :{
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'unregister': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'command' : {
            'handlers': ['command'],
            'level' : 'DEBUG',
            'propogate' : True
        }
    }
}

gettext = lambda s: s

BAD_WORDS = ['poop', ] #list of profanities
TIME_ZONE = "Africa/Kampala"
EMAIL_HOST_USER = ''
EMAIL_HOST = '127.0.0.1'
OPT_IN_WORDS = ["انضم","join"]
OPT_IN_WORDS_LUO=["donyo","dony","donyo","doyo",]
OPT_IN_WORDS_KDJ=["togeu","togu",'tog']
OPT_OUT_WORDS = ["استقال","quit"]

# map bounding box
MIN_LON = '29.55322265625'
MAX_LON = '33.92578125'
MIN_LAT = '-1.0326589311777759'
MAX_LAT = '4.280680030820496'
# map categorized color pallete
CATEGORY_COLORS = ['#AA4643', '#4572A7', '#89A54E', '#80699B', '#3D96AE', '#DB843D', '#92A8CD', '#A47D7C', '#B5CA92']

ADMINS = (
)


LANGUAGES = (
    ('ach', gettext('luo')),
    ('en', gettext('English')),
    ('ar', gettext('ar')),
)

LANGUAGE_CODE ="ar"
# you should configure your database here before doing any real work.
# see: http://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ureport',
        'HOST': 'db.ureport.org',
        'USER': 'postgres',
	'ROUTER_URL':'http://kannel.ureport.org:13013/cgi-bin/sendsms?from=8700&username=ureport&password=fake&text=%(text)s&to=%(recipient)s&smsc=%(backend)s&charset=utf-8&coding=2',
#	'OPTIONS': {
 #     	'autocommit': True,
  # 	},
 },
    'geoserver': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'geoserver',
        'HOST': 'db.ureport.org',
        'USER': 'postgres',
 },
}

MAP_BOUNDS = {'bottom_left': {'lon': 8.94, 'lat': 19.16},
              'top_right': {'lon': 26.43, 'lat': 33.88}
              }

MAP_ARGS = {'center': {'longitude': 17.22, 'latitude': 26.95},
	    'scale': 9000
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
# the valid options for each
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
    "tastypie",
    # the rapidsms contrib apps.
    "rapidsms.contrib.default",
    "rapidsms.contrib.locations",
    "rapidsms.contrib.locations.nested",
    "rapidsms.contrib.messagelog",
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
DEBUG = False
TEMPLATE_DEBUG = True

# after login (which is handled by django.contrib.auth), redirect to the
# dashboard rather than 'accounts/profile' (the default).
LOGIN_REDIRECT_URL = "/"


# use django-nose to run tests. rapidsms contains lots of packages and
# modules which django does not find automatically, and importing them
# all manually is tiresome and error-prone.
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"


# for some reason this setting is blank in django's global_settings.py,
# but it is needed for static assets to be linkable.
#MEDIA_URL = "/static/"
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
     'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    #'tracking.middleware.UserTrackingMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
     "ureport.middleware.permissions.RequirePermissionMiddleware",
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
#south stuff
SOUTH_TESTS_MIGRATE = False

USE_I18N = True
INITIAL_USSD_SCREEN='ussd_root'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
COUNTRY_SPECIFIC_TOKENS = {
    "district" : "county",
}

YES_WORDS = {"ar":["ﻦﻌﻣ","ﺄﺠﻟ","ﺐﻟﻯ"],"en":["yes","ya","y","yah","yey"]}

NO_WORDS = {"en":["no","nope","nah","nay","n"],"ar":["لا","أبدا"]}

# since we might hit the database from any thread during testing, the
# in-memory sqlite database isn't sufficient. it spawns a separate
# virtual database for each thread, and syncdb is only called for the
# first. this leads to confusing "no such table" errors. We create
# a named temporary instance instead.
import os
import tempfile
import sys

try:
    if os.environ.has_key('LOCAL_SETTINGS'):
        # the LOCAL_SETTINGS environment variable is used by the build server
        sys.path.insert(0, os.path.dirname(os.environ['LOCAL_SETTINGS']))
        from settings_test import *
    else:
        from localsettings import *
except ImportError:
    pass
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}







