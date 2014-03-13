from django.conf.urls import patterns, include, url
from basic import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.ind, name='main'),
    url(r'^basic/', include('basic.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
