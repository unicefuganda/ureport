# wsgi_app.py
import sys, os

filedir = os.path.dirname(__file__)
sys.path.append(os.path.join(filedir))

#print sys.path

os.environ["CELERY_LOADER"] = "django"
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import sys
print sys.path

from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
