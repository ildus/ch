#coding: utf-8

import models
from helpers import MAIN_PAGES

def pages(request):
    main_pages = []
    for one in MAIN_PAGES:
        try:
            if one == 'news':
                main_pages.append(one)
            else:
                page = models.Page.objects.get(alias = one)
                main_pages.append(page)
        except:
            pass
        
    try:
        phone = models.BottomBlock.objects.get(alias = 'phone')
    except:
        pass
    
    try:
        address = models.BottomBlock.objects.get(alias = 'address')
    except:
        pass
    
    try:
        copy = models.BottomBlock.objects.get(alias = 'copy')
    except:
        pass
    
    try:
        news_left = models.BottomBlock.objects.get(alias = 'news_left')
    except:
        pass
    
    try:
        news_right = models.BottomBlock.objects.get(alias = 'news_right')
    except:
        pass
        
    return locals()
    