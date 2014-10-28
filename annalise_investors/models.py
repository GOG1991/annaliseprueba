from django.db import models
from django.utils.translation import ugettext_lazy as _

CHOICES_GENERO = (('m', 'Masculino'), ('f', 'Femenino'),)
CHOICES_ESTADO_CIVIL = (('s', 'Soltero/a'), ('c', 'Casado/a'), ('d', 'Divorciado/a'), ('v', 'Viudo/a'))
CHOICES_CONTACTO = (('m', 'Telefono Movil'), ('c', 'Telefono de casa'), ('e', 'Email'))


class Pais(models.Model):
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"

    def __unicode__(self):
        return self.nombre


class EstadosPais(models.Model):
    pais = models.ForeignKey(Pais, verbose_name="Pais")
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    def __unicode__(self):
        return self.nombre


class Ciudad(models.Model):
    estado = models.ForeignKey(EstadosPais, verbose_name="Estado")
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __unicode__(self):
        return self.nombre


class InvestorUser(models.Model):
    nombres = models.CharField(max_length=50)
    apPaterno = models.CharField(max_length=50, verbose_name="Apellido paterno")
    apMaterno = models.CharField(max_length=50, verbose_name="Apellido materno")
    genero = models.CharField(max_length=1, choices=CHOICES_GENERO)
    fechNacimiento = models.DateField()
    pais = models.ForeignKey(Pais, verbose_name="Pais")
    estadoPais = models.ForeignKey(EstadosPais, verbose_name="Estado")
    ciudad = models.ForeignKey(Ciudad, verbose_name="Ciudad")
    estadoCivil = models.CharField(max_length=1, choices=CHOICES_ESTADO_CIVIL)
    curp = models.CharField(max_length=18, verbose_name="CURP")
    imss = models.CharField(max_length=12,verbose_name="Numero de seguro social (IMSS)")
    numHijos = models.IntegerField(verbose_name="Numero de hijos")
    colonia = models.CharField(max_length=100, verbose_name="Colonia")
    calle = models.CharField(max_length=100, verbose_name="Calle")
    numExterior = models.CharField(max_length=9, verbose_name="Numero exterior")
    numInterior = models.CharField(max_length=9, verbose_name="Numero interior", null=True, blank=True)
    telCasa = models.CharField(max_length=15, verbose_name="Telefono de casa")
    celular = models.CharField(max_length=15, verbose_name="Celular")
    contPrim = models.CharField(max_length=1, choices=CHOICES_CONTACTO, verbose_name="Contacto primario")
    contSec = models.CharField(max_length=1, choices=CHOICES_CONTACTO, verbose_name="Contacto secundario")

    class Meta:
        verbose_name = "Inversionista"
        verbose_name_plural = "Inversionistas"

    def __unicode__(self):
        return self.nombres
