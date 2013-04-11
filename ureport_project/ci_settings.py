from settings import *
IBM_TABLES_MANAGED = True
USE_NEW_START_POLL = False
INTERNAL_IPS = ('127.0.0.1')

GEOSERVER_URL = ""
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

#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#NOSE_ARGS = [
#    '--with-coverage',
#    '--cover-package=ureport',
#    ]
#TEST_RUNNER = 'django_test_coverage.runner.run_tests'
COMPUTE_COVERAGE="ureport"


