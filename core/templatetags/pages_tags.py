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
def page_url(alias, lang):
    try:
        page = Page.objects.get(alias = alias, language = lang)
        return page.lang_url(lang)
    except:
        return '#'
    
@register.simple_tag
def new_url(item, lang):
    try:
        return item.lang_url(lang)
    except:
        return '#'
    
@register.inclusion_tag('news_item.html', takes_context = True)
def news(context, count, is_center = 0):
    language = context['language']
    news = NewsItem.objects.filter(language = language)
    if count <= 10:
        news = news[:10]
    context['news'] = news
    context['is_center'] = is_center
    return context