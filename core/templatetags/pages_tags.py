# -*- coding: UTF-8 -*-
from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.template.context import RequestContext, Context
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db.models import F
from django.conf import settings

from core.models import Page, NewsItem

register = template.Library()

@register.simple_tag
def page_url(alias):
    try:
        page = Page.objects.get(alias = alias)
        return page.get_absolute_url()
    except:
        return '#'
    
@register.inclusion_tag('content.html', takes_context = True)
def tr(context, object, field):
    request = context['request']
    lang = request.LANGUAGE_CODE
    if hasattr(object, field) == False:
        return ''
    else:
        if lang == 'en':
            translated = getattr(object, field)
        if lang in ('ru', 'cn'):
            lang_field = '%s_%s' % (field, lang)
            translated = getattr(object, lang_field) if hasattr(object, lang_field) else ''
        
        if translated.strip() == '':
            lang = settings.LANGUAGE_CODE
            lang_field = '%s_%s' % (field, lang)
            translated = getattr(object, lang_field) if hasattr(object, lang_field) else ''
            
    if field in ('content', 'h1', 'right'):
        translated = mark_safe(translated)
    
    return {"value": translated }

@register.inclusion_tag('news_item.html', takes_context = True)
def news(context, count):
    news = NewsItem.objects.all()
    if count <= 10:
        news = news[:10]
    context['news'] = news
    return context