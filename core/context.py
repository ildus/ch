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
        
    try:
        footer = models.FooterText.objects.get(language = language)
    except:
        footer = None
        
    try:
        news_text = models.NewsPageTexts.objects.get(language = language)
    except:
        news_text = None
        
    data = {
        'main_pages': main_pages,
        'footer': footer,
        'news_text': news_text,
    }    
    return data