from django.conf.urls import patterns, include, url

from django.contrib import admin
from yawdadmin import admin_site

admin.autodiscover()
admin_site._registry.update(admin.site._registry)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin_site.urls)),
)
