from settings import *
ADMIN_UNREGISTER = True
IBM_TABLES_MANAGED = True
USE_NEW_START_POLL = False
INTERNAL_IPS = ('127.0.0.1')

#INSTALLED_APPS +=  ("django_nose",)

print "APPS : " + str(INSTALLED_APPS)

#south stuff
SOUTH_TESTS_MIGRATE = False

GEOSERVER_URL = ""

#Use the real dbs, don't create them
#os.environ['REUSE_DB'] = "1"

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ureport',
        'HOST': 'localhost',
        'USER': 'postgres',
        'ROUTER_URL' : "http://95.138.170.64:13013/cgi-bin/sendsms?from=8500&username=kannel&password=kannel&text=%(text)s&to=%(recipient)s&smsc=SMPPSim"
    },
    'geoserver': {
    'ENGINE' : 'django.db.backends.postgresql_psycopg2',
    'NAME': 'geoserver',
    'HOST': 'localhost',
    'USER': 'postgres',
    'ROUTER_URL':'http://95.138.170.64:13013/cgi-bin/sendsms?from=8500&username=kannel&password=kannel&text=%(text)s&to=%(recipient)s&smsc=SMPPSim'
   }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        }
}

INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.bucket",
    },
}

STATIC_URL="/static/media/"

COMPUTE_COVERAGE="ureport"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'command': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/ureport/command_log'
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'django_log_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/ureport/ureport_log.log',
            'formatter': 'simple',
            'backupCount': 50,
            'maxBytes': 2 ** 20,
        },
    },
    'loggers': {
        'rapidsms_ureport': {
            'handlers': ['django_log_file'],
            'level': 'INFO',
            'propagate': True,
            },
        'rapidsms_polls': {
            'handlers': ['django_log_file'],
            'level': 'INFO',
            'propagate': True,
            },
    'loggers': {
        'command': {
            'level': 'INFO',
            'handlers': ['command']
        }
    }
     }
}
