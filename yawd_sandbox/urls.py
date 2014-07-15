from django.conf.urls import patterns, include, url

from yawdadmin import admin_site

urlpatterns = patterns('',
    url(r'^admin/', include(admin_site.urls)),
)
