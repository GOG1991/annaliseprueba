# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'aplicant_vacancie'
        db.create_table(u'annalise_job_aplicant_vacancie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aplicant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Aplicante', to=orm['annalise_job.applicants'])),
            ('vacancie', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Vacante', to=orm['annalise_job.vacancies'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('ban', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'annalise_job', ['aplicant_vacancie'])

        # Adding model 'vacancies'
        db.create_table(u'annalise_job_vacancies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('published', self.gf('django.db.models.fields.DateTimeField')()),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'annalise_job', ['vacancies'])


    def backwards(self, orm):
        # Deleting model 'aplicant_vacancie'
        db.delete_table(u'annalise_job_aplicant_vacancie')

        # Deleting model 'vacancies'
        db.delete_table(u'annalise_job_vacancies')


    models = {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['annalise_job']