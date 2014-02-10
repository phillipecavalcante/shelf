from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shelf.views.home', name='home'),
    # url(r'^shelf/', include('shelf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/', include('apps.menu.urls', namespace='menu')),
    url(r'^pages/', include('apps.pages.urls', namespace='pages')),
    url(r'^gallery/', include('apps.gallery.urls', namespace='gallery')),
    url(r'^images/', include('apps.images.urls', namespace='images')),
    url(r'^search/', include('apps.exemplo.urls', namespace='search')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
#     url(r'^account/', include('account.urls', namespace='account')),
#     url(r'^', include('website.urls', namespace='website')),
)


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )