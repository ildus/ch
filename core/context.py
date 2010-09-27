#coding: utf-8

import models
from helpers import MAIN_PAGES

def pages(request):
    main_pages = []
    language = request.LANGUAGE_CODE
    for one in MAIN_PAGES:
        try:
            if one == 'news':
                main_pages.append(one)
            else:
                page = models.Page.objects.get(alias = one, language = language)
                main_pages.append(page)
        except:
            pass
        
    data = {
        'main_pages': main_pages,
    }
        
    fields = ('phone', 'address', 'copy', 'news_left', 'news_right')
    for one in fields:
        try:
            kwargs = {
                'alias': one,
                'language': language,
            }
            data[one] = models.BottomBlock.objects.get(**kwargs)
        except:
            pass
        
    return data
    