# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'blogs'
        db.create_table(u'annalise_cms_blogs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreBlog', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tagLine', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'annalise_cms', ['blogs'])

        # Adding model 'autores'
        db.create_table(u'annalise_cms_autores', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('userio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('nombreCompleto', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'annalise_cms', ['autores'])

        # Adding model 'categorias'
        db.create_table(u'annalise_cms_categorias', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreCategoria', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'annalise_cms', ['categorias'])

        # Adding model 'entradas'
        db.create_table(u'annalise_cms_entradas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('contenido', self.gf('tinymce.models.HTMLField')()),
            ('imgDestacada', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('pubDate', self.gf('django.db.models.fields.DateField')()),
            ('modDate', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('numComent', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('numPingbacks', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'annalise_cms', ['entradas'])

        # Adding M2M table for field categoria on 'entradas'
        m2m_table_name = db.shorten_name(u'annalise_cms_entradas_categoria')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entradas', models.ForeignKey(orm[u'annalise_cms.entradas'], null=False)),
            ('categorias', models.ForeignKey(orm[u'annalise_cms.categorias'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entradas_id', 'categorias_id'])


    def backwards(self, orm):
        # Deleting model 'blogs'
        db.delete_table(u'annalise_cms_blogs')

        # Deleting model 'autores'
        db.delete_table(u'annalise_cms_autores')

        # Deleting model 'categorias'
        db.delete_table(u'annalise_cms_categorias')

        # Deleting model 'entradas'
        db.delete_table(u'annalise_cms_entradas')

        # Removing M2M table for field categoria on 'entradas'
        db.delete_table(db.shorten_name(u'annalise_cms_entradas_categoria'))


    models = {
        u'annalise_cms.autores': {
            'Meta': {'object_name': 'autores'},
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreCompleto': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'userio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'annalise_cms.blogs': {
            'Meta': {'object_name': 'blogs'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreBlog': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'tagLine': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'annalise_cms.categorias': {
            'Meta': {'object_name': 'categorias'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreCategoria': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'annalise_cms.entradas': {
            'Meta': {'ordering': "['-pubDate']", 'object_name': 'entradas'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['annalise_cms.categorias']", 'symmetrical': 'False'}),
            'contenido': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgDestacada': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modDate': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'numComent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numPingbacks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pubDate': ('django.db.models.fields.DateField', [], {}),
            'rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['annalise_cms']