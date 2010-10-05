#coding: utf-8

from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    (r'^admin/', include(admin.site.urls)),
    url(r'^i18n/setlang/', 'core.views.set_language', name = 'setlang'),
    url(r'^(?:(en|ru|zh)/)?$', 'core.views.index', name = 'index'),
    url(r'^(?:(en|ru|zh)/)?news/$', 'core.views.news', name = 'news'),
    url(r'^((?P<language>(?:(en|ru|zh)))/)?news/(?P<alias>[-\w]+)/$', 'core.views.news_item', name = 'news_item'),
)

if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )