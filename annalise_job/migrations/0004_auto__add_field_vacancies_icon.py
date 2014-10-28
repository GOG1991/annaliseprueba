# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'vacancies.icon'
        db.add_column(u'annalise_job_vacancies', 'icon',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'vacancies.icon'
        db.delete_column(u'annalise_job_vacancies', 'icon')


    models = {
        u'annalise_investors.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['annalise_investors.EstadosPais']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'annalise_investors.estadospais': {
            'Meta': {'object_name': 'EstadosPais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['annalise_investors.Pais']"})
        },
        u'annalise_investors.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'annalise_job.aplicant_vacancie': {
            'Meta': {'object_name': 'aplicant_vacancie'},
            'aplicant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Aplicante'", 'to': u"orm['annalise_job.applicants']"}),
            'ban': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vacancie': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Vacante'", 'to': u"orm['annalise_job.vacancies']"})
        },
        u'annalise_job.applicants': {
            'Meta': {'object_name': 'applicants'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['annalise_investors.Ciudad']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_application': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vacante': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['annalise_job.vacancies']", 'null': 'True', 'through': u"orm['annalise_job.aplicant_vacancie']", 'blank': 'True'})
        },
        u'annalise_job.vacancies': {
            'Meta': {'object_name': 'vacancies'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['annalise_job']