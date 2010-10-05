# -*- coding: UTF-8 -*-
'''
Created on 06.06.2010

@author: sivirk
'''
import helpers
from django.core.exceptions import ObjectDoesNotExist

class Page:
    def process_response(self,request,response):
        if response.status_code == 404:
            try:
                response = helpers.get_page(request)
            except ObjectDoesNotExist:
                pass
            except:
                pass
            
        return response