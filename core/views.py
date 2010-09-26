# coding: utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from helpers import activate_language

from models import NewsItem

def index(request, language = None):
    language = language or 'ru'
    activate_language(language)
    return direct_to_template(request, template = 'index.html', extra_context = {'language': language})

def news(request, language = None):
    language = language or 'ru'
    activate_language(language)    
    return direct_to_template(request, template = 'news.html', extra_context = {'is_news': True, 'language': language})

def news_item(request, language = None, alias = None):
    language = language or 'ru'
    object = get_object_or_404(NewsItem, alias = alias)
    return direct_to_template(request, template = 'page.html', extra_context = {'object': object, 'language': language})