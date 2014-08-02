# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Parallax'
        db.create_table(u'djangocms_parallax_parallax', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('speed', self.gf('django.db.models.fields.DecimalField')(default='0.2', max_digits=3, decimal_places=2)),
            ('cover_ratio', self.gf('django.db.models.fields.DecimalField')(default='0.75', max_digits=3, decimal_places=2)),
            ('holder_min_height', self.gf('django.db.models.fields.IntegerField')(default=200)),
        ))
        db.send_create_signal(u'djangocms_parallax', ['Parallax'])

        # Adding model 'ParallaxImage'
        db.create_table(u'djangocms_parallax_parallaximage', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('extra_height', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'djangocms_parallax', ['ParallaxImage'])

        # Adding model 'ParallaxContent'
        db.create_table(u'djangocms_parallax_parallaxcontent', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
        ))
        db.send_create_signal(u'djangocms_parallax', ['ParallaxContent'])


    def backwards(self, orm):
        # Deleting model 'Parallax'
        db.delete_table(u'djangocms_parallax_parallax')

        # Deleting model 'ParallaxImage'
        db.delete_table(u'djangocms_parallax_parallaximage')

        # Deleting model 'ParallaxContent'
        db.delete_table(u'djangocms_parallax_parallaxcontent')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'djangocms_parallax.parallax': {
            'Meta': {'object_name': 'Parallax', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'cover_ratio': ('django.db.models.fields.DecimalField', [], {'default': "'0.75'", 'max_digits': '3', 'decimal_places': '2'}),
            'holder_min_height': ('django.db.models.fields.IntegerField', [], {'default': '200'}),
            'speed': ('django.db.models.fields.DecimalField', [], {'default': "'0.2'", 'max_digits': '3', 'decimal_places': '2'})
        },
        u'djangocms_parallax.parallaxcontent': {
            'Meta': {'object_name': 'ParallaxContent', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'})
        },
        u'djangocms_parallax.parallaximage': {
            'Meta': {'object_name': 'ParallaxImage', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'extra_height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['djangocms_parallax']