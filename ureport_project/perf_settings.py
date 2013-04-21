from ci_settings import *

print "!!! RUNNING AGAINST THE PERFORMANCE DB!!!!"

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ureport_prod',
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

CELERY_ALWAYS_EAGER = False
