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
    blocks = models.BottomBlock.objects.all()[:3]
        
    return locals()
    