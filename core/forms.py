#coding: utf-8

from treebeard.forms import MoveNodeForm
from django import forms
from django.contrib.admin.widgets import AdminTextInputWidget
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from core.models import BasePage, Page

class BasePageForm(forms.ModelForm):
    #def textarea(cols, rows):
    #    return forms.Textarea(attrs = {'rows': rows, 'cols': cols})
#    
    meta_description = forms.CharField(label = _('Description'), widget = AdminTextInputWidget(),
                                            help_text = _('meta tag "description"'), required = False)
    meta_keywords = forms.CharField(label = _('Keywords'), widget = AdminTextInputWidget(),
                                            help_text = _('meta tag "keywords"'), required = False)
    
    class Media:
        css = {
            'all': (settings.MEDIA_URL+'core/css/admin_basepage.css', ),
        }
        
        js = (
            settings.MEDIA_URL+'js/admin_basepage.js',
        )
        
    class Meta:
        model = BasePage
    
class PageForm(BasePageForm, MoveNodeForm):
    class Meta:
        model = Page
