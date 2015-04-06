from django.conf.urls import patterns, include, url
from django.contrib import admin
from bracket.views import viewTeam, home, Source
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marchmadness.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^$', 'bracket.views.home', name = 'home'),
	url(r'^team/(?P<id>[0-9]+)/$', viewTeam, name = 'viewTeam'),
	url(r'^sources/$', Source, name = 'Source'),
    url(r'^admin/', include(admin.site.urls)),
)
