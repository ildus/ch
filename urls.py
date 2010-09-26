#coding: utf-8

from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^(?:(en|ru|cn)/)?$', 'core.views.index', name = 'index'),
    url(r'^(?:(en|ru|cn)/)?news/$', 'core.views.news', name = 'news'),
    url(r'^((?P<language>(?:(en|ru|cn)))/)?news/(?P<alias>[-\w]+)/$', 'core.views.news_item', name = 'news_item'),

    (r'^admin/', include(admin.site.urls)),
)

if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )