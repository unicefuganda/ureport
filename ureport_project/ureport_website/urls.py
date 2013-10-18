# ureport_website/urls.py

from django.conf.urls.defaults import patterns, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group


admin.autodiscover()
admin.site.unregister(Site)
admin.site.unregister(Group)

urlpatterns = patterns(
    '',
    url(r'^$', 'ureport_website.views.index', name="website-index"),
    url(r'^about-ureport$', 'ureport_website.views.about', name='website-about-ureport'),

    url(r'^engage$', TemplateView.as_view(template_name='engage.html'), name='website-engage'),
    url(r'^polls$', TemplateView.as_view(template_name='polls.html'), name='website-polls'),
    url(r'^polls-list$', TemplateView.as_view(template_name='polls_list.html'), name='website-polls'),
    url(r'^national-pulse$', TemplateView.as_view(template_name='national_pulse.html'), name='website-national-pulse'),

    url(r'^partners$', 'ureport_website.views.partners', name='website-partners'),
    url(r'^partners/(?P<slug>[\w\-]+)/$', 'ureport_website.views.partnersDetail'),

    url(r'^read$', 'ureport_website.views.readArticles', name='website-read'),
    url(r'^read/(?P<slug>[\w\-]+)/$', 'ureport_website.views.readDetail'),

    url(r'^watch$', 'ureport_website.views.watch', name='website-watch'),
    url(r'^watch/(?P<slug>[\w\-]+)/$', 'ureport_website.views.watchDetail', name='website-watch-detail'),
)
