#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
# encoding=utf-8

import djcelery
djcelery.setup_loader()

# -------------------------------------------------------------------- #
#                          PATH CONFIGURATION                          #
# -------------------------------------------------------------------- #

import os
import sys


PROJECT_PATH = os.path.join(os.path.dirname(__file__), os.pardir)

sys.path.append(os.path.join(PROJECT_PATH))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms', 'lib'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_auth'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_contact'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_cvs'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_generic'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_geoserver'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_httprouter_src'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_polls'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_script'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_uregister'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_ureport'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_uganda_common'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_unregister'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_xforms_src'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_tracking'))
sys.path.append(os.path.join(PROJECT_PATH, 'django_eav'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_uganda_ussd'))
sys.path.append(os.path.join(PROJECT_PATH, 'rapidsms_message_classifier'))
sys.path.append(os.path.join(PROJECT_PATH, 'qos_monitor'))

gettext = lambda s: s

# -------------------------------------------------------------------- #
#                          MAIN CONFIGURATION                          #
# -------------------------------------------------------------------- #
BAD_WORDS = ['poop', ]  # list of profanities
TIME_ZONE = "Africa/Kampala"
EMAIL_HOST_USER = ''
EMAIL_HOST = '127.0.0.1'
OPT_IN_WORDS = ['join']
OPT_IN_WORDS_LUO = ["donyo", "dony", "donyo", "doyo"]
OPT_IN_CONFIRMATION = gettext("Welcome to UReport! Ureport is a community of "
                              "%(citizen)s youth that are dedicated to "
                              "working for positive change in their "
                              "communities. Stay tuned for more info.")\
    % {"citizen": gettext("Ugandan")}

OPT_OUT_WORDS = ['stop', 'unjoin', 'quit', 'giki']
OPT_OUT_CONFIRMATION = gettext("Your UReport opt out is confirmed.If you "
                               "made a mistake,or you want your voice to be "
                               "heard again,text in JOIN and send it to "
                               "8500!All SMS messages are free")

# map bounding box
MIN_LON = '29.55322265625'
MAX_LON = '33.92578125'
MIN_LAT = '-1.0326589311777759'
MAX_LAT = '4.280680030820496'
# map categorized color pallete
CATEGORY_COLORS = ['#AA4643', '#4572A7', '#89A54E', '#80699B', '#3D96AE',
                   '#DB843D', '#92A8CD', '#A47D7C', '#B5CA92']

ADMINS = (
)


LANGUAGES = (
    ('ach', gettext('luo')),
    ('en', gettext('English')),

)

# you should configure your database here before doing any real work.
# see: http://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ureport',
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
    "rapidsms.contrib.messagelog",
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
    "django_nose"  # Except nose must come after south so that migrations run!!
]

SMS_APPS = [
    "unregister",
    "monitor",
    "ureport",
    "script",
    "poll",
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

# this is used for geoserver to tell which website this viz should be for
# (and prevents clashing of polls across different websites with the same id)
DEPLOYMENT_ID = 1

#model containing blacklisted contacts
BLACKLIST_MODEL = "unregister.Blacklist"

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
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'uganda_common.middleware.accessmiddleware.accessmiddleware.AccessMiddleWare',
    #'tracking.middleware.UserTrackingMiddleware',
    #'ureport.middleware.permissions.RequirePermissionMiddleware',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'command': {
            'class': 'logging.FileHandler',
            'filename': '/var/log/ureport/command.log',
            'formatter': 'simple'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'application_log_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/ureport/ureport_application.log',
            'formatter': 'verbose',
            'backupCount': 50,
            'maxBytes': 2 ** 20,
        },
        'application_access_log_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/ureport/ureport_access.log',
            'formatter': 'verbose',
            'backupCount': 50,
            'maxBytes': 2 ** 20,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['application_log_file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'ureport': {
            'handlers': ['application_log_file'],
            'level': 'INFO',
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
            'level': 'INFO',
            'propagate': True,
        },
        'ureport.tasks': {
            'handlers': ['application_log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'ureport.views.poll_views': {
            'handlers': ['application_log_file'],
            'level': 'INFO',
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
            'level': 'INFO',
            'propagate': True,
        },
        'rapidsms_httprouter.views': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'rapidsms_httprouter.router': {
            'handlers': ['application_log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'unregister': {
            'handlers': ['application_log_file'],
            'level': 'INFO',
            'propagate': True,
        },
        'script.utils.outgoing': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'script.managers': {
            'handlers': ['application_log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'command': {
            'handlers': ['command'],
            'level': 'DEBUG',
            'propogate': True
        }
    }
}

# -------------------------------------------------------------------- #
#                         CELERY CONFIGURATION                         #
# -------------------------------------------------------------------- #

# djcelery can load config from here, so this replaces celeryconfig.py

CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_PERSISTENT = False
CELERY_TASK_RESULT_EXPIRES = 10
CELERY_DISABLE_RATE_LIMITS = True
CELERY_SEND_TASK_ERROR_EMAILS = True

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = {
    'default': {
        'binding_key': 'task.#',
    },
    'upload_responses': {
        'binding_key': 'upload_responses.#',
    },
    'classify_excel': {
        'binding_key': 'classify_excel.#',
    },
    'message_export': {
        'binding_key': 'message_export.#',
    },
    'start_poll': {
        'binding_key': 'start_poll.#',
    },
    'process_message': {
        'binding_key': 'process_message.#',
    },
    'handle_incoming': {
        'binding_key': 'handle_incoming.#',
    },
    'reprocess_responses': {
        'binding_key': 'reprocess_responses.#',
    },
    'push_to_mtrac': {
        'binding_key': 'push_to_mtrac.#'
    },
    'process_uploaded_contacts': {
        'binding_key': 'process_uploaded_contacts.#'
    },
    'process_assign_group': {
        'binding_key': 'process_assign_group.#'
    },
    'export_poll': {
        'binding_key': 'export_poll.#'
    },
    'extract_gen_reports': {
        'binding_key': 'extract_gen_reports.#'
    }
}
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'
#CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_USER = "ureport"
BROKER_PASSWORD = "ureport"
BROKER_VHOST = "ureport"

CELERY_ROUTES = {
    'message_classifier.tasks.upload_responses': {
        'queue': 'upload_responses',
        'routing_key': 'upload_responses.result'
    },
    'message_classifier.tasks.classify_excel': {
        'queue': 'classify_excel',
        'routing_key': 'classify_excel.result'
    },
    'message_classifier.tasks.message_export': {
        'queue': 'message_export',
        'routing_key': 'message_export.result'
    },
    'ureport.tasks.start_poll': {
        'queue': 'start_poll',
        'routing_key': 'start_poll.result'
    },
    'ureport.tasks.process_message': {
        'queue': 'process_message',
        'routing_key': 'process_message.result'
    },
    'rapidsms_httprouter.tasks.handle_incoming': {
        'queue': 'handle_incoming',
        'routing_key': 'handle_incoming.result'
    },
    'ureport.tasks.reprocess_responses': {
        'queue': 'reprocess_responses',
        'routing_key': 'reprocess_responses.result'
    },
    'ureport.tasks.push_to_mtrac': {
        'queue': 'push_to_mtrac',
        'routing_key': 'push_to_mtrac.result'
    },
    'ureport.tasks.process_uploaded_contacts': {
        'queue': 'process_uploaded_contacts',
        'routing_key': 'process_uploaded_contacts.result'
    },
    'ureport.tasks.process_assign_group': {
        'queue': 'process_assign_group',
        'routing_key': 'process_assign_group.result'
    },
    'ureport.tasks.export_poll': {
        'queue': 'export_poll',
        'routing_key': 'export_poll.result'
    },
    'ureport.tasks.extract_gen_reports': {
        'queue': 'extract_gen_reports',
        'routing_key': 'extract_gen_reports.result'
    }

}

SERVER_EMAIL = 'Ureport Background Tasks<background@ureport.ug>'

CELERY_IMPORTS = ('ureport.tasks', 'message_classifier.tasks',
                  'rapidsms_httprouter.tasks')

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
INITIAL_USSD_SCREEN = 'ussd_root'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

SHOW_CONTACT_INFO = False

USE_NEW_START_POLL = False
ADMIN_UNREGISTER = False

## Testing settings:
## http://hustoknow.blogspot.com/2011/02/setting-up-django-nose-on-hudson.html
# https://nose.readthedocs.org/en/latest/plugins/cover.html
# this is supposed to exclude a dir '--exclude-dir=',
NOSE_ARGS = ('--with-xunit', '--with-coverage',
             '--cover-html', '--verbosity=2',
             '--xunit-file=target/reports/unit-test/nosetests.ureport.xml',
             '--cover-html-dir=target/reports/unit-test/coverage',
             '--cover-package=poll,uganda_common,unregister,'
             'message_classifier,contact,rapidsms_httprouter,rapidsms_ureport',
             )

MAP_BOUNDS = {
    'bottom_left': {'lon': 28.6963, 'lat': -1.8015},
    'top_right': {'lon': 35.8592, 'lat': 4.9}
}

#MAP_BOUNDS SHOULD MOVE INTO HERE (BEFORE GEOSERVER IS KILLED)
MAP_ARGS = {'center': {'longitude': 32.27, 'latitude': 0.95},
            'scale': 23000
            }

COUNTRY_SPECIFIC_TOKENS = {
    "district": "district"
}

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)
# since we might hit the database from any thread during testing, the
# in-memory sqlite database isn't sufficient. it spawns a separate
# virtual database for each thread, and syncdb is only called for the
# first. this leads to confusing "no such table" errors. We create
# a named temporary instance instead.

PAGINATION_LIMIT = None

BACKENDS_CONFIGURATION = {
    "vumi": {
        "ENGINE": "rapidsms.backends.vumi.VumiBackend",
        "sendsms_url": "http://2.2.2.1:9000/send/",
        "sendsms_user": "username",
        "sendsms_pass": "password",
    }
}

try:
    if 'LOCAL_SETTINGS' in os.environ:
        # the LOCAL_SETTINGS environment variable is used by the build server
        sys.path.insert(0, os.path.dirname(os.environ['LOCAL_SETTINGS']))
        from settings_test import *
    else:
        from localsettings import *
except ImportError:
    pass
# if 'test' in sys.argv:
#     DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
