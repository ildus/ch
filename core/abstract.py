#coding: utf-8

from django.contrib import admin
from tagging.fields import TagField
from lib.fields import TagsWidget, TinyMCEEditor
from django.db import models


class BasePageAdmin(admin.ModelAdmin):
    '''
        Базовый класс для всех админок моделей, которые имеют свои страницы 
    '''
    
    prepopulated_fields = {"alias": ("name",), }
    list_filter = ('active',)
    
    search_fields = ('name','title','h1',)
    char_filter = ('name',)
    
    formfield_overrides = {
        TagField: {'widget': TagsWidget},
        models.TextField: {'widget': TinyMCEEditor}
    }