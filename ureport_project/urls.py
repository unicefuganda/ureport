from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from rapidsms_httprouter.urls import urlpatterns as router_urls
from ureport.urls import urlpatterns as ureport_urls
from contact.urls import urlpatterns as contact_urls
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_change
from tracking.urls import urlpatterns as tracking_urls
from generic.urls import urlpatterns as generic_urls
from django.views.generic.simple import direct_to_template
from ussd.urls import urlpatterns as ussd_urls
from message_classifier.urls import urlpatterns as class_urls
#from script.urls import urlpatterns as script_urls
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),

    # RapidSMS core URLs
    (r'^account/', include('rapidsms.urls.login_logout')),
    url(r'^$', direct_to_template, {'template':'ureport/home.html'}, name="new_home"),
    url(r'^join/$', direct_to_template, {'template':'ureport/how_to_join.html'}),
    url(r'^about_ureport/$', direct_to_template, {'template':'ureport/about.html'}),
    url(r'^ureport-admin$', 'ureport.views.ureport_content', {'slug':'ureport_home', 'base_template':'ureport/three-square.html', 'num_columns':3}, name='rapidsms-dashboard'),
    url('^accounts/login', 'rapidsms.views.login'),
    url('^accounts/logout', 'rapidsms.views.logout'),
    url('^accounts/change_password', login_required(password_change), {'template_name':'ureport/change_password.html', 'post_change_redirect':'/'}),
    url(r'^national-pulse/$', direct_to_template, {'template': 'ureport/national_pulse.html'}, name='pulse'),
    url(r'^national-pulse-mock/$', direct_to_template, {'template': 'ureport/national_pulse_mock.html'}),
    # RapidSMS contrib app URLs
    url(r'^ajax/', include('rapidsms.contrib.ajax.urls')),
    url(r'^export/', include('rapidsms.contrib.export.urls')),
    url(r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    url(r'^locations/', include('rapidsms.contrib.locations.urls')),
    url(r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    url(r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    url(r'^registration/', include('auth.urls')),
    url(r'^scheduler/', include('rapidsms.contrib.scheduler.urls')),
    url(r'^polls/', include('poll.urls')),
    
) + router_urls + ureport_urls + contact_urls + tracking_urls + generic_urls+ ussd_urls+class_urls


if settings.DEBUG:
    urlpatterns += patterns('',
        # helper URLs file that automatically serves the 'static' folder in
        # INSTALLED_APPS via the Django static media server (NOT for use in
        # production)
        (r'^', include('rapidsms.urls.static_media')),
    )

from rapidsms_httprouter.router import get_router
get_router(start_workers=True)
