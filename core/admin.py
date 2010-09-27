# coding: utf-8

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from lib.extensions.tree_editor import TreeEditor, ajax_editable_boolean

from lib.fields import TagsWidget, TinyMCEEditor
from tagging.fields import TagField

from django.db import models

import core.forms
import core.models
from abstract import BasePageAdmin

class PageAdmin(BasePageAdmin, TreeEditor):
    list_display = ('name', 'alias', 'language', 'url', 'active_toggle')        
    active_toggle = ajax_editable_boolean('active', _('is active'))
    
    form = core.forms.PageForm
    
    fieldsets = (
        (_('Options'), {
            'fields': ('alias', 'active', 'meta_redirect', 'language'),
        }),
        ( _('Text'), {
            'fields':( ('name', 'title'), 'h1', 'content', 'right')
        }),
              
        (_('Meta'), {
            'fields': ( 'meta_description','meta_keywords'),
        }),
        (_('Tree location'), {
            'fields': ( ('_position', '_ref_node_id',),  ),
        }),
    )
    
class NewsAdmin(BasePageAdmin):
    list_display = ('name', 'alias', 'language')
    
    form = core.forms.BasePageForm
    
    fieldsets = (
        (_('Options'), {
            'fields': ('alias', 'active', 'meta_redirect', 'language'),
        }), 
        ( _('Text'), {
            'fields':( ('name', 'title'), 'h1', 'content', 'right')
        }),    
        (_('Meta'), {
            'fields': ( 'meta_description','meta_keywords'),
        }),
    )
    
class BottomAdmin(admin.ModelAdmin):
    list_display = ('alias', 'language')
    from django.db import models
    from lib.fields.widgets import TinyMCEEditor
    formfield_overrides = {
        models.TextField : {"widget" : TinyMCEEditor}
    }
    
admin.site.register(core.models.Page, PageAdmin)
admin.site.register(core.models.NewsItem, NewsAdmin)
admin.site.register(core.models.BottomBlock, BottomAdmin)