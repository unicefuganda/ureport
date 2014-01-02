import copy
from .base import *

DEBUG = TEMPLATE_DEBUG = False
GEOSERVER_URL = ''

# -------------------------------------------------------------------- #
#                         CACHE CONFIGURATION                         #
# -------------------------------------------------------------------- #
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

CACHING_MIDDLEWARES = (
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + CACHING_MIDDLEWARES


# -------------------------------------------------------------------- #
#                         SENTRY CONFIGURATION                         #
# -------------------------------------------------------------------- #
LOGGING['handlers']['sentry'] = {
    'level': 'ERROR',
    'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
}
LOGGING['root'] = {
    'level': 'WARNING',
    'handlers': ['sentry'],
}
LOGGING['loggers']['raven'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}
LOGGING['loggers']['sentry.errors'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}

# raven docs say to put SentryResponseErrorIdMiddleware
# 'as high in the chain as possible'
# so this will insert raven into the top of the base
# settings.py file's MIDDLEWARE_CLASSES
TEMP = list(copy.copy(MIDDLEWARE_CLASSES))
TEMP.insert(0, 'raven.contrib.django.raven_compat.'
               'middleware.SentryResponseErrorIdMiddleware')
TEMP.append('raven.contrib.django.raven_compat.'
            'middleware.Sentry404CatchMiddleware')
MIDDLEWARE_CLASSES = tuple(TEMP)

INSTALLED_APPS += ("raven.contrib.django.raven_compat",)

# TODO we should support SSL
RAVEN_CONFIG = {
    'dsn': 'http://fa310d8c078c40cb9881fdb787ba21c1:'
           '42d834d6923740ee88e1027e7e213941@sentry.unicefuganda.org/2',
}

SENTRY_URL = "http://sentry.unicefuganda.org/t4d/ureport/"

CELERY_QUEUES["sentry"] = {
    "exchange": "default",
    "binding_key": "sentry"
}
