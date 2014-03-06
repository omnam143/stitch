from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'onam.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^openhealth/', include('basic.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
