# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import permalink
from tinymce.widgets import TinyMCE


class blogs(models.Model):
    nombreBlog = models.CharField(max_length=100, verbose_name='Nombre del blog')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion del blog', null=True, blank=True)
    tagLine = models.CharField(max_length=100, verbose_name='Etiquetas', null=True, blank=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.nombreBlog


class autores(models.Model):
    userio = models.ForeignKey(User, unique=True, verbose_name='Usuario')
    nombreCompleto = models.CharField(max_length=150, verbose_name='Nombre Completo', null=True, blank=True)
    direccion = models.CharField(max_length=150, verbose_name='Direccion', null=True, blank=True)
    telefono = models.CharField(max_length=20, verbose_name='Telefono', null=True, blank=True)
    celular = models.CharField(max_length=20, verbose_name='Celular', null=True, blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombreCompleto


class categorias(models.Model):
    nombreCategoria = models.CharField(max_length=100, verbose_name='Nombre')
    slug = models.SlugField(max_length=100, db_index=True)
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombreCategoria

    @permalink
    def getAbsoluteUrl(self):
        return ('categorias', None, {'slug': self.slug})


estado = (('d', 'Borrador'), ('p', 'Publicado'),)


class entradas(models.Model):
    titulo = models.CharField(max_length=300, verbose_name='Titulo')
    slug = models.SlugField(max_length=100, unique=True)
    contenido = HTMLField()
    categoria = models.ManyToManyField(categorias, verbose_name='Categorias')
    imgDestacada = models.ImageField(upload_to='uploads', blank=True, null=True, verbose_name='Imagen destacada')
    pubDate = models.DateField(verbose_name='Fecha de publicacion', auto_now_add = True)
    modDate = models.DateField(verbose_name='Fecha de modificacion', auto_now=True)
    usuario = models.ForeignKey(User)
    numComent = models.IntegerField(editable=False, null=True, blank=True)
    numPingbacks = models.IntegerField(editable=False, null=True, blank=True)
    rating = models.IntegerField(editable=False, null=True, blank=True)
    status = models.CharField(max_length=1, choices=estado)

    class Meta:
        ordering = ['-pubDate']
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.titulo

    @permalink
    def getAbsoluteUrl(self):
        return ('entradas', None, {'slug': self.slug})
