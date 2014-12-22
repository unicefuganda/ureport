from settings import *
CELERY_ALWAYS_EAGER = True
ADMIN_UNREGISTER = True
IBM_TABLES_MANAGED = True
INTERNAL_IPS = ('127.0.0.1')
FEATURE_PREPARE_SEND_POLL=False

# These MUST be set or the message will not be classified!
NO_WORDS = {'en':['no', 'nope', 'nah', 'nay', 'n'],
            'ach':['ku', 'k','pe'],
            'kdj':["emam",'ema'],
}
OPT_IN_WORDS_KDJ=["togeu","togu",'tog']
OPT_OUT_WORDS = ['stop', 'unjoin', 'quit','giki','unsub','unsubscribe','stop ureport','unregister','deactivate']

#INSTALLED_APPS +=  ("django_nose",)

#print "APPS : " + str(INSTALLED_APPS)

#south stuff
SOUTH_TESTS_MIGRATE = False

#Use the real dbs, don't create them
#os.environ['REUSE_DB'] = "1"

NOSE_ARGS = ( )


GEOSERVER_URL = "/geoserver/"
TEST_SERVER_URL = "http://localhost"

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ureport',
        'HOST': 'localhost',
        'USER': 'postgres',
        'ROUTER_URL': "http://127.0.0.1:13013/cgi-bin/sendsms?from=8500&username=kannel&password=kannel&text=%(text)s&to=%(recipient)s&smsc=SMPPSim"
    },
    'geoserver': {
    'ENGINE' : 'django.db.backends.postgresql_psycopg2',
    'NAME': 'geoserver',
    'HOST': '127.0.0.1',
    'USER': 'postgres',
   }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 0,
        'OPTIONS': {
            'MAX_ENTRIES': 1
        }
    }
}

INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.bucket",
    },
}

STATIC_URL="/static/media/"
ADMIN_MEDIA_PREFIX="/media/"

COMPUTE_COVERAGE="ureport"

import logging
south_logger=logging.getLogger('south')
south_logger.setLevel(logging.INFO)

logging.disable(logging.CRITICAL)
