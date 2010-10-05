# coding: utf-8

from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template
from helpers import activate_language

from models import NewsItem, Metadata
from django.contrib.csrf.middleware import csrf_exempt

from django import http
from django.conf import settings
from django.utils import importlib
from django.utils.translation import check_for_language
from django.utils.text import javascript_quote
from django.utils.encoding import smart_unicode
from django.utils.formats import get_format_modules

@csrf_exempt
def set_language(request):
    """
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'POST':
        lang_code = request.POST.get('language', None)
        if lang_code and check_for_language(lang_code):
            if hasattr(request, 'session'):
                request.session['django_language'] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
    return response

def index(request, language = None):
    language = language or 'ru'
    try:
        metadata = Metadata.objects.get(location = 'main', language = language)
    except:
        metadata = None    
    activate_language(request, language)
    return direct_to_template(request, template = 'index.html', extra_context = {'language': language, 'metadata': metadata})

def news(request, language = None):
    language = language or 'ru'
    activate_language(request, language)    
    return direct_to_template(request, template = 'news.html', extra_context = {'is_news': True, 'language': language})

def news_item(request, language = None, alias = None):
    language = language or 'ru'
    activate_language(request, language)
    object = get_object_or_404(NewsItem, alias = alias, language = language)
    return direct_to_template(request, template = 'page.html', extra_context = {'is_news': True, 'object': object, 'language': language})