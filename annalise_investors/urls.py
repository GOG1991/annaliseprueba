from django.conf.urls import patterns, include, url

urlpatterns = patterns('annalise_investors.views',
                       url(r'^investors/$', 'investorsView', name='investors'),
                       url(r'^ok/$', 'ok', name='ok'),
)
