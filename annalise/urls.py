from django.conf.urls import patterns, include, url, handler404, handler500
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    (r'',include('annalise_cms.urls')),
    (r'',include('annalise_job.urls')),
    (r'',include('annalise_investors.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'', include('django.contrib.flatpages.urls')),
    
)


if settings.DEBUG:
        urlpatterns += patterns('',
             url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),)

handler404 = "annalise_cms.views.error404"
handler500 = "annalise_cms.views.error500"

