from django.conf.urls import patterns, include, url
from django.conf import settings

from .views import tiendasView

urlpatterns = patterns('annalise_cms.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^tiendas/', tiendasView.as_view(), name='tiendas'),
                       url(r'^(?P<slug>[-\w]+).html$', 'single', name='single'),
                       url(r'^blog/$', 'news', name='blog'),
                       url(r'^promociones/$', 'promos', name='promociones'),
                       url(r'^productos/$', 'productsView', name='products'),
                       url(r'^contacto/$', 'contacto', name='contacto'),
                       url(r'^search/$', 'search', name='search'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }), )