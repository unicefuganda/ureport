# ureport_website/urls.py

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from .views import SiteIndexView
from .views import AboutView
from .views import EngageView
from .views import NationalPulseView
from .views import PollsListView
from .views import PollDetailView
from .views import PartnersListView
from .views import PartnersDetailView
from .views import ReadListView

urlpatterns = patterns(
    '',
    url(
        r'^$',
        SiteIndexView.as_view(),
        name="website-index"
    ),
    url(
        '^about-ureport$',
        AboutView.as_view(),
        name="website-about-ureport"
    ),
    url(
        r'^engage$',
        EngageView.as_view(),
        name='website-engage'
    ),
    url(
        r'^national-pulse$',
        NationalPulseView.as_view(),
        name='website-national-pulse'
    ),

    # Polls
    url(
        r'^polls/$',
        PollsListView.as_view(),
        name='website-polls'
    ),
    url(
        r'^polls/(?P<object_id>\d+)/$',
        PollDetailView.as_view(),
        name='website-polls-detail'
    ),

    # Partners
    url(
        r'^partners$',
        PartnersListView.as_view(),
        name='website-partners'
    ),
    url(
        r'^partners/(?P<slug>[\w\-]+)/$',
        PartnersDetailView.as_view(),
        name='website-partners-detail'
    ),

    # Read
    url(
        r'^read$',
        ReadListView.as_view(),
        name='website-read'
    ),
    url(r'^read/(?P<slug>[\w\-]+)/$', 'ureport_website.views.readDetail'),

    url(r'^watch$', 'ureport_website.views.watch', name='website-watch'),
    url(r'^watch/(?P<slug>[\w\-]+)/$', 'ureport_website.views.watchDetail', name='website-watch-detail'),
)
