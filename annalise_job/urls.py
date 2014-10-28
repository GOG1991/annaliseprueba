from django.conf.urls import patterns, include, url

urlpatterns = patterns('annalise_job.views',
	url(r'^captcha/', include('captcha.urls')),
	url(r'^vacantes/$', 'vacanciesList', name = 'vacantes'),
	url(r'^vacantes/(?P<slug>[-\w]+).html$', 'vacancie_single', name = 'vacante' ),
	url(r'^vacantes/(\d+)/$','dataApplicant', name = 'aplicar'),

)
