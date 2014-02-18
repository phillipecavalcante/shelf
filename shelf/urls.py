#===============================================================================
# DJANGO
#===============================================================================
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shelf.views.home', name='home'),
    # url(r'^shelf/', include('shelf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include('apps.dashboard.urls', namespace='dashboard')),
    url(r'^menu/', include('apps.menu.urls', namespace='menu')),
    url(r'^pages/', include('apps.pages.urls', namespace='pages')),
    url(r'^gallery/', include('apps.gallery.urls', namespace='gallery')),
    url(r'^images/', include('apps.images.urls', namespace='images')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^accounts/', include('apps.account.urls', namespace='account')),
    url(r'^', include('apps.website.urls', namespace='website')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
