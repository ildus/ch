# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Page.name_ch'
        db.delete_column('core_page', 'name_ch')

        # Deleting field 'Page.right_ch'
        db.delete_column('core_page', 'right_ch')

        # Deleting field 'Page.content_ch'
        db.delete_column('core_page', 'content_ch')

        # Deleting field 'Page.h1_ch'
        db.delete_column('core_page', 'h1_ch')

        # Deleting field 'Page.title_ch'
        db.delete_column('core_page', 'title_ch')

        # Adding field 'Page.h1_cn'
        db.add_column('core_page', 'h1_cn', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Page.title_cn'
        db.add_column('core_page', 'title_cn', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Page.name_cn'
        db.add_column('core_page', 'name_cn', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True), keep_default=False)

        # Adding field 'Page.content_cn'
        db.add_column('core_page', 'content_cn', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'Page.right_cn'
        db.add_column('core_page', 'right_cn', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Page.name_ch'
        db.add_column('core_page', 'name_ch', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # We cannot add back in field 'Page.right_ch'
        raise RuntimeError(
            "Cannot reverse this migration. 'Page.right_ch' and its values cannot be restored.")

        # We cannot add back in field 'Page.content_ch'
        raise RuntimeError(
            "Cannot reverse this migration. 'Page.content_ch' and its values cannot be restored.")

        # We cannot add back in field 'Page.h1_ch'
        raise RuntimeError(
            "Cannot reverse this migration. 'Page.h1_ch' and its values cannot be restored.")

        # We cannot add back in field 'Page.title_ch'
        raise RuntimeError(
            "Cannot reverse this migration. 'Page.title_ch' and its values cannot be restored.")

        # Deleting field 'Page.h1_cn'
        db.delete_column('core_page', 'h1_cn')

        # Deleting field 'Page.title_cn'
        db.delete_column('core_page', 'title_cn')

        # Deleting field 'Page.name_cn'
        db.delete_column('core_page', 'name_cn')

        # Deleting field 'Page.content_cn'
        db.delete_column('core_page', 'content_cn')

        # Deleting field 'Page.right_cn'
        db.delete_column('core_page', 'right_cn')


    models = {
        'core.newsitem': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'NewsItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
