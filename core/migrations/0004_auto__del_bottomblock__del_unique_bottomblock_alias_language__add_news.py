# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'BottomBlock', fields ['alias', 'language']
        db.delete_unique('core_bottomblock', ['alias', 'language'])

        # Deleting model 'BottomBlock'
        db.delete_table('core_bottomblock')

        # Adding model 'NewsPageTexts'
        db.create_table('core_newspagetexts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('text_left', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('text_right', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('core', ['NewsPageTexts'])


    def backwards(self, orm):
        
        # Adding model 'BottomBlock'
        db.create_table('core_bottomblock', (
            ('alias', self.gf('django.db.models.fields.SlugField')(max_length=50, db_index=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('text', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('core', ['BottomBlock'])

        # Adding unique constraint on 'BottomBlock', fields ['alias', 'language']
        db.create_unique('core_bottomblock', ['alias', 'language'])

        # Deleting model 'NewsPageTexts'
        db.delete_table('core_newspagetexts')


    models = {
        'core.footertext': {
            'Meta': {'object_name': 'FooterText'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'text1': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text2': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text3': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text4': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'core.newsitem': {
            'Meta': {'ordering': "('-created',)", 'object_name': 'NewsItem'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alias': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'h1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'ru'", 'max_length': '2'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_redirect': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'right': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'core.newspagetexts': {
            'Meta': {'object_name': 'NewsPageTexts'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'text_left': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'text_right': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'core.page': {
            'Meta': {'ordering': "('tree_id', 'depth')", 'object_name': 'Page'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'alias': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'h1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indexed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'ru'", 'max_length': '2'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta_redirect': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rgt': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'right': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']
