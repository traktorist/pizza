from django.conf.urls import patterns, include, url
from orderpizza.views import times

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', times),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
