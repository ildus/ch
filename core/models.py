#coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

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
    
    objects = PageManager()
    
    #h1
    h1 = models.CharField('H1', max_length = 255, blank=True, help_text=_('tag H1'))
    h1_cn = models.CharField('H1', max_length = 255, blank=True, help_text=_('tag H1'))
    h1_ru = models.CharField('H1', max_length = 255, blank=True, help_text=_('tag H1'))
    
    #title
    title = models.CharField(_('title'), max_length = 255, blank=True, 
                                                    help_text=_('tag "title"'))
    title_cn = models.CharField(_('title'), max_length = 255, blank=True, 
                                                    help_text=_('tag "title"'))
    title_ru = models.CharField(_('title'), max_length = 255, blank=True, 
                                                    help_text=_('tag "title"'))
    
    #name
    name = models.CharField(_('name'), max_length = 255, blank = True)
    name_cn = models.CharField(_('china name'), max_length = 255, blank = True)
    name_ru = models.CharField(_('russian name'), max_length = 255)
    
    #content
    content = models.TextField(_('english content'), blank = True)
    content_cn = models.TextField(_('china content'), blank = True)
    content_ru = models.TextField(_('russian content'))
    
    #right
    right = models.TextField(_('Right column'), blank = True)
    right_cn = models.TextField(_('Right column (ch)'), blank = True)
    right_ru = models.TextField(_('Right column (ru)'))
    
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
        return "%s/%s/" % (p, self.alias)
    
    def lang_url(self, lang = None):
        lang = lang or 'ru'
        return '/%s%s' % (lang, self.get_absolute_url())
        
    def save(self,*args,**kwargs):
        self.url = self.get_absolute_url()
        return super(Page,self).save(*args,**kwargs)
        
    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        ordering = ('tree_id', 'depth')
        
class NewsItem(BasePage):
    created = models.DateTimeField(_("Creating date"), default = datetime.now)
    
    def lang_url(self, lang = None):
        lang = lang or 'ru'
        return '/%s%s' % (lang, self.get_absolute_url())
    
    class Meta:
        verbose_name = _('news Item')
        verbose_name_plural = _('news')
        ordering = ('-created', )
        
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('news_item', args = [self.alias])
        
class BottomBlock(models.Model):
    CH = (
        ('copy', 'copy'),
        ('address', 'address'),
        ('phone', 'phone'),
        ('news_left', 'Text on Left Side of News Page'),
        ('news_right', 'Text on Right Side of News Page'),
    )
    
    alias = models.SlugField(choices = CH, unique = True)
    
    text_ru = models.TextField("RU")
    text_cn = models.TextField("CN", blank = True)
    text = models.TextField("EN", blank = True)
    
    def __unicode__(self):
        return self.alias
    
    class Meta:
        verbose_name = _("text")
        verbose_name_plural = _("texts")
        
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
