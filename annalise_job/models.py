# -*- encoding: utf-8 -*-
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from annalise_investors.models import Ciudad

'''
class typevacancies(models.Model):
	name = models.CharField(_('Nombre del tipo de vacante'), max_length=100)
	description = models.TextField(_('Descripcion del tipo de vacante'), null=True, blank=True)

	class Meta:
		verbose_name = _('Tipo de vacante')
		verbose_name_plural = _('Tipos de vacantes')

	def __unicode__(self):
		return self.name
'''
tv = ((''))
class vacancies(models.Model):
	title = models.CharField(_('Titulo de la vacante'), max_length=100)
	slug = models.SlugField(max_length=150, unique=True)
	description = models.TextField(_('Descripcion de la vacante'))
	published = models.DateTimeField(verbose_name = "Fecha de publicación", editable=False)
	visible = models.BooleanField(_('Disponible'),default=True)
	#typev = models.ForeignKey(typevacancies, verbose_name = 'Tipo de vacante', default = 1)
	icon = models.ImageField(upload_to='uploads', blank=True, null=True, verbose_name='Icono de la vacante')

	class Meta:
		verbose_name = _('Vacante')
		verbose_name_plural = _('Vacantes')


	def save(self,*args,**kwars):
		if not self.id:
			self.published = timezone.now()
		return super(vacancies,self).save(*args, **kwars)

	@permalink
	def getAbsoluteUrl(self):
		return ('vacancies',None,{'slug':self.slug})

	def __unicode__(self):
		return self.title


op = (('m', 'Masculino'),('f', 'Femenino'),)
class applicants(models.Model):
	name = models.CharField(_('Nombre(s)'), max_length = 50)
	last_name = models.CharField(_('Apellidos'), max_length = 50)
	address = models.CharField(_('Domicilio'), max_length = 50)
	city = models.ForeignKey(Ciudad, default=None, null=True,blank=True)
	email = models.EmailField(_('Email'), max_length = 75)
	gender = models.CharField(_('Genero'), max_length = 1, choices = op)
	job_application = models.FileField(_('Curriculum'), upload_to = 'documents/%Y/%m/%d')
	vacante = models.ManyToManyField(vacancies, through = 'aplicant_vacancie', null=True, blank=True)

	class Meta:
		verbose_name = _('Aplicante')
		verbose_name_plural =_('Aplicantes')

	def __str__(self):
		return self.name


class aplicant_vacancie(models.Model):
	aplicant = models.ForeignKey(applicants, related_name='Aplicante')
	vacancie = models.ForeignKey(vacancies, related_name='Vacante')
	date = models.DateTimeField(editable=True)
	ban = models.BooleanField(_('Tomo la vacante'), default=False)

	class Meta:
		verbose_name = _('Aplicante de la vacante')
		verbose_name_plural = _('Aplicantes de la vacante')

	def __unicode__(self):
		return '%s - %s' % (self.aplicant, self.vacancie)


	def save(self,*args,**kwars):
		if not self.id:
			self.date=timezone.now()
		return super(aplicant_vacancie,self).save(*args,**kwars)