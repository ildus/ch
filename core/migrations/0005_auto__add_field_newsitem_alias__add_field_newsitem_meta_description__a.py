# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'NewsItem.alias'
        db.add_column('core_newsitem', 'alias', self.gf('django.db.models.fields.SlugField')(default='2010-09-25 10:19:03.339845', max_length=50, db_index=True), keep_default=False)

        # Adding field 'NewsItem.meta_description'
        db.add_column('core_newsitem', 'meta_description', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'NewsItem.meta_keywords'
        db.add_column('core_newsitem', 'meta_keywords', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'NewsItem.meta_redirect'
        db.add_column('core_newsitem', 'meta_redirect', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.active'
        db.add_column('core_newsitem', 'active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'NewsItem.indexed'
        db.add_column('core_newsitem', 'indexed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'NewsItem.h1'
        db.add_column('core_newsitem', 'h1', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.h1_cn'
        db.add_column('core_newsitem', 'h1_cn', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.h1_ru'
        db.add_column('core_newsitem', 'h1_ru', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.title'
        db.add_column('core_newsitem', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.title_cn'
        db.add_column('core_newsitem', 'title_cn', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.title_ru'
        db.add_column('core_newsitem', 'title_ru', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.name'
        db.add_column('core_newsitem', 'name', self.gf('django.db.models.fields.CharField')(default='2010-09-25 10:19:19.987848', max_length=255), keep_default=False)

        # Adding field 'NewsItem.name_cn'
        db.add_column('core_newsitem', 'name_cn', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.name_ru'
        db.add_column('core_newsitem', 'name_ru', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'NewsItem.content'
        db.add_column('core_newsitem', 'content', self.gf('django.db.models.fields.TextField')(default='2010-09-25 10:19:36.392887'), keep_default=False)

        # Adding field 'NewsItem.content_cn'
        db.add_column('core_newsitem', 'content_cn', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'NewsItem.content_ru'
        db.add_column('core_newsitem', 'content_ru', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'NewsItem.right'
        db.add_column('core_newsitem', 'right', self.gf('django.db.models.fields.TextField')(default='2010-09-25 10:19:47.696216'), keep_default=False)

        # Adding field 'NewsItem.right_cn'
        db.add_column('core_newsitem', 'right_cn', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'NewsItem.right_ru'
        db.add_column('core_newsitem', 'right_ru', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'NewsItem.alias'
        db.delete_column('core_newsitem', 'alias')

        # Deleting field 'NewsItem.meta_description'
        db.delete_column('core_newsitem', 'meta_description')

        # Deleting field 'NewsItem.meta_keywords'
        db.delete_column('core_newsitem', 'meta_keywords')

        # Deleting field 'NewsItem.meta_redirect'
        db.delete_column('core_newsitem', 'meta_redirect')

        # Deleting field 'NewsItem.active'
        db.delete_column('core_newsitem', 'active')

        # Deleting field 'NewsItem.indexed'
        db.delete_column('core_newsitem', 'indexed')

        # Deleting field 'NewsItem.h1'
        db.delete_column('core_newsitem', 'h1')

        # Deleting field 'NewsItem.h1_cn'
        db.delete_column('core_newsitem', 'h1_cn')

        # Deleting field 'NewsItem.h1_ru'
        db.delete_column('core_newsitem', 'h1_ru')

        # Deleting field 'NewsItem.title'
        db.delete_column('core_newsitem', 'title')

        # Deleting field 'NewsItem.title_cn'
        db.delete_column('core_newsitem', 'title_cn')

        # Deleting field 'NewsItem.title_ru'
        db.delete_column('core_newsitem', 'title_ru')

        # Deleting field 'NewsItem.name'
        db.delete_column('core_newsitem', 'name')

        # Deleting field 'NewsItem.name_cn'
        db.delete_column('core_newsitem', 'name_cn')

        # Deleting field 'NewsItem.name_ru'
        db.delete_column('core_newsitem', 'name_ru')

        # Deleting field 'NewsItem.content'
        db.delete_column('core_newsitem', 'content')

        # Deleting field 'NewsItem.content_cn'
        db.delete_column('core_newsitem', 'content_cn')

        # Deleting field 'NewsItem.content_ru'
        db.delete_column('core_newsitem', 'content_ru')

        # Deleting field 'NewsItem.right'
        db.delete_column('core_newsitem', 'right')

        # Deleting field 'NewsItem.right_cn'
        db.delete_column('core_newsitem', 'right_cn')

        # Deleting field 'NewsItem.right_ru'
        db.delete_column('core_newsitem', 'right_ru')


    models = {
        'core.bottomblock': {
            'Meta': {'object_name': 'BottomBlock'},
            'first': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'second': ('django.db.models.fields.TextField', [], {}),
            'third': ('django.db.models.fields.TextField', [], {})
        },
        'core.newsitem': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'NewsItem'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alias': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_cn': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_ru': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'h1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'h1_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'h1_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_redirect': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'right': ('django.db.models.fields.TextField', [], {}),
            'right_cn': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'right_ru': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'core.page': {
            'Meta': {'ordering': "('tree_id', 'depth')", 'object_name': 'Page'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alias': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_cn': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_ru': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'h1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'h1_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'h1_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_redirect': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rgt': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'right': ('django.db.models.fields.TextField', [], {}),
            'right_cn': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'right_ru': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title_cn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']
