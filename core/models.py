#coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from treebeard.ns_tree import NS_Node
from datetime import datetime

from lib.fields import RichTextField

class PageManager(models.Manager):
    
    def active(self):
        qs = self.get_query_set().filter(active=True)
        return qs
    
class BasePage(models.Model):
    '''
        Абстрактная модель для всех объектов которые могут иметь собственную страницу.
    '''
    
    alias = models.SlugField(_('alias'))
    
    meta_description = models.TextField(_('description'), blank = True, 
                                     help_text = _('meta tag "description"'))
    meta_keywords = models.TextField(_('keywords'), blank = True, 
                                     help_text = _('meta tag "keywords"'))
    meta_redirect = models.CharField(_('redirect'), max_length = 255, 
                                     blank = True, help_text = _('http 302'))
    active = models.BooleanField(_('active'), default=True)
    
    #поле необходимое для поиска
    indexed = models.DateTimeField(_('indexed'), null = True, blank = True, editable = False)   
    language = models.CharField(max_length = 2, choices = settings.LANGUAGES, default = 'ru')
    
    objects = PageManager()
    
    h1 = models.CharField('H1', max_length = 255, blank=True, help_text=_('tag H1'))
    title = models.CharField(_('title'), max_length = 255, blank=True, help_text=_('tag "title"'))
    name = models.CharField(_('name'), max_length = 255, blank = True)
    content = models.TextField(_('content'), blank = True)
    right = models.TextField(_('Right column'), blank = True)
    
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name
    
    def save(self):
        self.indexed = None
        super(BasePage, self).save()
    
class Page(BasePage, NS_Node):
        
    url = models.CharField(max_length=255, editable=False)    
    
    def get_absolute_url(self):
        parents = self.get_ancestors()
        p = ''
        if parents:
            for one in parents:
                p += '/%s'%(one.alias)
        return "/%s%s/%s/" % (self.language, p, self.alias)
        
    def save(self,*args,**kwargs):
        self.url = self.get_absolute_url()
        return super(Page,self).save(*args,**kwargs)
        
    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        ordering = ('tree_id', 'depth')
        
class NewsItem(BasePage):
    created = models.DateTimeField(_("Creating date"), default = datetime.now)
    
    class Meta:
        verbose_name = _('news Item')
        verbose_name_plural = _('news')
        ordering = ('-created', )
        
    def get_absolute_url(self):
        return "/%s/news/%s/" % (self.language, self.alias)
        
class BottomBlock(models.Model):
    CH = (
        ('copy', 'copy'),
        ('address', 'address'),
        ('phone', 'phone'),
        ('news_left', 'Text on Left Side of News Page'),
        ('news_right', 'Text on Right Side of News Page'),
    )
    
    alias = models.SlugField(choices = CH)
    language = models.CharField(max_length = 2, choices = settings.LANGUAGES)
    text = models.TextField(_("Text"), blank = True)
    
    def __unicode__(self):
        return self.alias
    
    class Meta:
        verbose_name = _("text")
        verbose_name_plural = _("texts")
        unique_together = (("alias", "language"),)
        
def page_deleted(sender, **kwargs):
    instance = kwargs['instance']
    children = instance.get_children()
    if children:
        if instance.is_root():
            another_root = Page.get_first_root_node() or \
                    Page.add_root(name = '_temp', alias = '_temp', content = '_temp')
            for node in children:
                node.move(another_root, pos='first-sibling')
            if another_root.name == '_temp':
                another_root.delete()
        else:
            parent = instance.get_parent()
            for node in children:
                node.move(parent, 'last-child')
            
from django.db.models.signals import pre_delete
pre_delete.connect(page_deleted, sender = Page)
