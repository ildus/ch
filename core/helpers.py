# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext


import core.models
from django.utils import translation
from django.utils.translation import check_for_language

MAIN_PAGES = ('about', 'services', 'news', 'contacts')

def activate_language(request, lang_code):
    translation.activate(lang_code or 'ru')
    if lang_code and check_for_language(lang_code):
        if hasattr(request, 'session'):
            request.session['django_language'] = lang_code
            
def get_page(request):
    '''
        Получаем респонз страницы
    '''
    path =  request.path
    elems = request.path.split('/')
    language = None
    if len(elems) > 1:
        if elems[1] in ('ru', 'en', 'zh'):
            language = elems[1]
            activate_language(request, elems[1])
        else:
            activate_language(request, 'ru')
    object =  get_object_or_404(core.models.Page,url=path)
    if object.meta_redirect:
        return redirect(object.meta_redirect)
    else:
        language = language or 'ru'
        return render_to_response("page.html",locals(),RequestContext(request))