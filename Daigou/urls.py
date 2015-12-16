from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Daigou.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^%ssearch/' % settings.BASE_URL, include('haystack.urls')),
    url(r'^%s' % settings.BASE_URL, views.home),

    url(r'^%sthisisadmin/' % settings.BASE_URL, include(admin.site.urls)),
)
