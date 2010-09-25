# coding: utf-8

from django.shortcuts import render_to_response, get_object_or_404
from django.views.generic.simple import direct_to_template

from models import NewsItem

def index(request):
    return direct_to_template(request, template = 'index.html')

def news(request):
    return direct_to_template(request, template = 'news.html', extra_context = {'is_news': True})

def news_item(request, alias):
    object = get_object_or_404(NewsItem, alias = alias)
    return direct_to_template(request, template = 'page.html', extra_context = {'object': object})