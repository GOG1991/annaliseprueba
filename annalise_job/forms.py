# -*- encoding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import applicants, aplicant_vacancie
from captcha.fields import CaptchaField

class applicantForm(forms.ModelForm):
	captcha = CaptchaField(label='Codigo de verificación')

	class Meta:
		model = applicants
		exclude = ('vacante',)
		labels = {
            'city': _('Ciudad'),
        }
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control input-lg ','name':'txtname','id':'txtname'}),
			'last_name': forms.TextInput(attrs={'class':'form-control input-lg',}),
			'address': forms.TextInput(attrs={'class':'form-control input-lg',}),
			'city': forms.Select(attrs={'class':'form-control input-lg',}),
			'email': forms.TextInput(attrs={'class':'form-control input-lg',}),
			'gender': forms.Select(attrs={'class':'form-control input-lg',}),
			'job_application':forms.ClearableFileInput(attrs={'class':'form-control fileCurri'}),
		}

class aplicantVacancieForm(forms.ModelForm):

	class Meta:
		model = aplicant_vacancie
		exclude = ('aplicant','ban','date',)
		widgets={
			'vacancie':forms.HiddenInput(attrs={'class':'txtVacante','id':'txtVacante'}),
		}
		