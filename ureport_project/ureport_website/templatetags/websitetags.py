from django import template
from django.template.defaultfilters import stringfilter
from django.core.urlresolvers import get_resolver
from datetime import datetime
from django.conf import settings
from urlparse import parse_qs
import re
import urlparse

BOOTSTRAP_BASE_URL = getattr(settings, 'BOOTSTRAP_BASE_URL',
                             '/static/'
)

BOOTSTRAP_JS_BASE_URL = getattr(settings, 'BOOTSTRAP_JS_BASE_URL',
                                BOOTSTRAP_BASE_URL + 'js/'
)

BOOTSTRAP_JS_URL = getattr(settings, 'BOOTSTRAP_JS_URL',
                           None
)

BOOTSTRAP_CSS_BASE_URL = getattr(settings, 'BOOTSTRAP_CSS_BASE_URL',
                                 BOOTSTRAP_BASE_URL + 'css/'
)

BOOTSTRAP_CSS_URL = getattr(settings, 'BOOTSTRAP_CSS_URL',
                            BOOTSTRAP_CSS_BASE_URL + 'bootstrap.css'
)

THEME_CSS_URL = getattr(settings, 'THEME_CSS_URL',
                            BOOTSTRAP_CSS_BASE_URL + 'style.css'
)

register = template.Library()

@stringfilter
def youtube_thumbnail(value, args):
    qs = value.split('?')
    video_id = parse_qs(qs[1])['v'][0]

    if args == 's':
        return "http://img.youtube.com/vi/%s/0.jpg" % video_id
    elif args == 'l':
        return "http://i1.ytimg.com/vi/%s/mqdefault.jpg" % video_id
    else:
        return None

register.filter('youtube_thumbnail', youtube_thumbnail)

@stringfilter
def youtube_embed(value):
    qs = value.split('?')
    video_id = parse_qs(qs[1])['v'][0]
    return "//youtube.com/embed/%s" % video_id

register.filter('youtube_embed', youtube_embed)

@register.simple_tag
def bootstrap_stylesheet_url(css=None):
    """
    URL to Bootstrap Stylesheet (CSS)
    """
    url = 'BOOTSTRAP_CSS_URL'
    if css:
        url = BOOTSTRAP_CSS_BASE_URL + u'bootstrap-%s.css' % css
    else:
        url = BOOTSTRAP_CSS_URL
    return url


@register.simple_tag
def theme_stylesheet_url(css=None):
    """
    URL to Theme Stylesheet (CSS)
    """
    url = THEME_CSS_URL
    return url    


@register.simple_tag
def bootstrap_stylesheet_tag(css=None):
    """
    HTML tag to insert Bootstrap stylesheet
    """
    return u'<link rel="stylesheet" href="%s">' % bootstrap_stylesheet_url(css)


@register.simple_tag
def theme_stylesheet_tag(css=None):
    """
    HTML tag to insert Theme stylesheet
    """
    return u'<link rel="stylesheet" href="%s">' % theme_stylesheet_url(css) 

#add favicon tag
@register.simple_tag
def favicon_tag(css=None):
    """
    HTML tag to insert favicon
    """
    url = BOOTSTRAP_BASE_URL + 'ico/favicon.png'
    return u'<link rel="shortcut icon" href="%s">' % url

@register.simple_tag
def bootstrap_javascript_url(name=None):
    """
    URL to Bootstrap javascript file
    """
    if BOOTSTRAP_JS_URL:
        return BOOTSTRAP_JS_URL
    if name:
        return BOOTSTRAP_JS_BASE_URL + 'bootstrap-' + name + '.js'
    else:
        return BOOTSTRAP_JS_BASE_URL + 'bootstrap.min.js'


@register.simple_tag
def bootstrap_javascript_tag(name=None):
    """
    HTML tag to insert bootstrap javascript file
    """
    url = bootstrap_javascript_url(name)
    if url:
        return u'<script src="%s"></script>' % url
    return u'' 