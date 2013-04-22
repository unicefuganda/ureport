import os

print "django_wsgi.py : DJANGO_SETTINGS_MODULE is set to be [" + os.environ['DJANGO_SETTINGS_MODULE'] + "]"



import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
