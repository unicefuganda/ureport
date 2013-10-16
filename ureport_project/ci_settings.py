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

GEOSERVER_URL = "/geoserver/"
TEST_SERVER_URL = "http://162.13.95.58"

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
            'filename': '/var/log/ureport/command.log',
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

        'selenium.webdriver.remote.remote_connection' : {
            'handlers': ['application_log_file'],
            'level': 'ERROR',
            'propagate': True,
         },

        'django' : {
            'handlers': ['application_log_file'],
            'level': 'ERROR',
            'propagate': True,
        
        },

        'app/ureport' : {
            'handlers': ['application_log_file'],
            'level': 'INFO',
            'propagate': True,
        
        },

        'app/ureport' : {
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

        # 'command': {
        #     'level': 'DEBUG',
        #     'handlers': ['command']
        # },
        'command' : {
            'handlers': ['command'],
            'level' : 'DEBUG',
            'propogate' : True
        }
     }
}
