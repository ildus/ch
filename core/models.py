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
    
    meta_description = models.TextField(_('description'), blank = True, help_text = _('meta tag "description"'))
    meta_keywords = models.TextField(_('keywords'), blank = True, help_text = _('meta tag "keywords"'))
    meta_redirect = models.CharField(_('redirect'), max_length = 255,  blank = True, help_text = _('http 302'))
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
        if self.language != 'ru':
            return "/%s%s/%s/" % (self.language, p, self.alias)
        else:
            return '%s/%s/' % (p, self.alias)
        
    def get_url(self):
        parents = self.get_ancestors()
        p = ''
        if parents:
            for one in parents:
                p += '/%s'%(one.alias)
        return "/%s%s/%s/" % (self.language, p, self.alias)
        
    def save(self,*args,**kwargs):
        self.url = self.get_url()
        return super(Page,self).save(*args,**kwargs)
        
    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        ordering = ('tree_id', 'depth')
        
class NewsItem(BasePage):
    anonce = models.TextField("Anounce", max_length = 2000, blank = True)
    created = models.DateTimeField(_("Creating date"), default = datetime.now)
    
    class Meta:
        verbose_name = _('news Item')
        verbose_name_plural = _('news')
        ordering = ('-created', )
        
    def get_absolute_url(self):
        if self.language != 'ru':
            return "/%s/news/%s/" % (self.language, self.alias)
        else:
            return "/news/%s/" % (self.alias)
        
class NewsPageTexts(models.Model):
    language = models.CharField(max_length = 2, choices = settings.LANGUAGES, unique = True)
    text_left = models.TextField(_("Text On Left"), blank = True)
    text_right = models.TextField(_("Text On Right"), blank = True)
    
    def __unicode__(self):
        return "Texts for language '%s'" % self.language
    
    class Meta:
        verbose_name = _("news page texts")
        verbose_name_plural = _("news page texts")
        
class FooterText(models.Model):
    language = models.CharField(max_length = 2, choices = settings.LANGUAGES, unique = True)
    text1 = models.TextField(_("Text 1"), blank = True)
    text2 = models.TextField(_("Text 2"), blank = True)
    text3 = models.TextField(_("Text 3"), blank = True)
    text4 = models.TextField(_("Text 4"), blank = True)
    
    def __unicode__(self):
        return "Footer for language '%s'" % self.language
    
    class Meta:
        verbose_name = _("footer texts")
        verbose_name_plural = _("footer texts")
        
class Metadata(models.Model):
    LOCATIONS = (
        ('main', 'Main Page'),
    )
    
    language = models.CharField(max_length = 2, choices = settings.LANGUAGES, default = 'ru')
    location = models.CharField(_("Location"), unique = True, choices = LOCATIONS, max_length = 30)
    title = models.CharField(max_length = 1000,verbose_name = u'Title',blank=True,help_text=u'Тег title')
    
    meta_description = models.TextField(verbose_name=u'Description',blank=True,help_text=u'Мета тег description')
    meta_keywords = models.TextField(verbose_name=u'Keywords',blank=True,help_text=u'Мета тег keywords')
    
    def __unicode__(self):
        return "%s %s" % (self.location, self.language)
    
    class Meta:
        verbose_name = 'metadata'
        verbose_name_plural = 'metadata'
        unique_together = ('location', 'language')
        
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
