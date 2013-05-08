from ci_settings import *

print "!!! RUNNING AGAINST THE PERFORMANCE DB!!!!"

FEATURE_PREPARE_SEND_POLL=True

DEBUG = False # You want this on if we are going to see exceptions in the logs

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ureport_prod',
        'HOST': 'localhost',
        'USER': 'postgres',
        'ROUTER_URL' : "http://localhost:8084/cgi-bin/sendsms?from=8500&username=kannel&password=kannel&text=%(text)s&to=%(recipient)s&smsc=SMPPSim",
        'AUTOCOMMIT' : 'False'
    },
    'geoserver': {
    'ENGINE' : 'django.db.backends.postgresql_psycopg2',
    'NAME': 'geoserver',
    'HOST': 'localhost',
    'USER': 'postgres',
    'ROUTER_URL':'http://localhost:8084/cgi-bin/sendsms?from=8500&username=kannel&password=kannel&text=%(text)s&to=%(recipient)s&smsc=SMPPSim'
   }
}

CELERY_ALWAYS_EAGER = False
