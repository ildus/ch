# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext


import core.models
from django.utils import translation

MAIN_PAGES = ('about', 'services', 'news', 'contacts')

def activate_language(language):
    if language == 'cn': language = 'zh'
    translation.activate(language or 'ru')

class PageDoesNotExist(Exception):
    '''
        Страница не существует
    '''    
    pass


def get_page(request):
    '''
        Получаем респонз страницы
    '''
    path =  request.path
    elems = request.path.split('/')
    language = None
    if len(elems) > 1:
        if elems[1] in ('ru', 'en', 'cn'):
            language = elems[1]
            activate_language(elems[1])
            del elems[1]
            path = '/'.join(elems)
        else:
            activate_language('ru')
    object =  get_object_or_404(core.models.Page,url=path)
    if object.meta_redirect:
        return redirect(object.meta_redirect)
    else:
        language = language or 'ru'
        return render_to_response("page.html",locals(),RequestContext(request))