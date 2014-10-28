# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pais'
        db.create_table(u'annalise_investors_pais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'annalise_investors', ['Pais'])

        # Adding model 'EstadosPais'
        db.create_table(u'annalise_investors_estadospais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['annalise_investors.Pais'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'annalise_investors', ['EstadosPais'])

        # Adding model 'Ciudad'
        db.create_table(u'annalise_investors_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['annalise_investors.EstadosPais'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'annalise_investors', ['Ciudad'])

        # Adding model 'InvestorUser'
        db.create_table(u'annalise_investors_investoruser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombres', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('apPaterno', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('apMaterno', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('genero', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('fechNacimiento', self.gf('django.db.models.fields.DateField')()),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['annalise_investors.Pais'])),
            ('estadoPais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['annalise_investors.EstadosPais'])),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['annalise_investors.Ciudad'])),
            ('estadoCivil', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('curp', self.gf('django.db.models.fields.CharField')(max_length=18)),
            ('imss', self.gf('django.db.models.fields.IntegerField')()),
            ('numHijos', self.gf('django.db.models.fields.IntegerField')()),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('numExterior', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('numInterior', self.gf('django.db.models.fields.CharField')(max_length=9, null=True, blank=True)),
            ('telCasa', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('contPrim', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('contSec', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'annalise_investors', ['InvestorUser'])


    def backwards(self, orm):
        # Deleting model 'Pais'
        db.delete_table(u'annalise_investors_pais')

        # Deleting model 'EstadosPais'
        db.delete_table(u'annalise_investors_estadospais')

        # Deleting model 'Ciudad'
        db.delete_table(u'annalise_investors_ciudad')

        # Deleting model 'InvestorUser'
        db.delete_table(u'annalise_investors_investoruser')


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
        u'annalise_investors.investoruser': {
            'Meta': {'object_name': 'InvestorUser'},
            'apMaterno': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'apPaterno': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['annalise_investors.Ciudad']"}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contPrim': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'contSec': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'curp': ('django.db.models.fields.CharField', [], {'max_length': '18'}),
            'estadoCivil': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'estadoPais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['annalise_investors.EstadosPais']"}),
            'fechNacimiento': ('django.db.models.fields.DateField', [], {}),
            'genero': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imss': ('django.db.models.fields.IntegerField', [], {}),
            'nombres': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'numExterior': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'numHijos': ('django.db.models.fields.IntegerField', [], {}),
            'numInterior': ('django.db.models.fields.CharField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['annalise_investors.Pais']"}),
            'telCasa': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'annalise_investors.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['annalise_investors']