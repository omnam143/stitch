from django.conf.urls import patterns, url

from basic import views

urlpatterns = patterns('',
    url(r'^(?P<alphabet>\w)/$', views.index, name='index'),
    url(r'^ind/$', views.ind, name='ind')
)
