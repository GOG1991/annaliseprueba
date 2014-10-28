# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'InvestorUser.imss'
        db.alter_column(u'annalise_investors_investoruser', 'imss', self.gf('django.db.models.fields.CharField')(max_length=12))

    def backwards(self, orm):

        # Changing field 'InvestorUser.imss'
        db.alter_column(u'annalise_investors_investoruser', 'imss', self.gf('django.db.models.fields.IntegerField')())

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
            'imss': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
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