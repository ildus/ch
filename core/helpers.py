# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template.context import RequestContext


import core.models

MAIN_PAGES = ('about', 'services', 'news', 'contacts')

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
    object =  get_object_or_404(core.models.Page,url=path)
    if object.meta_redirect:
        return redirect(object.meta_redirect)
    else:
        return render_to_response("page.html",locals(),RequestContext(request))