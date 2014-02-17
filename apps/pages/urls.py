#===============================================================================
# DJANGO
#===============================================================================
from django.conf.urls import patterns, url
#===============================================================================
# PAGES
#===============================================================================
from apps.pages.views import *
from django.contrib.auth.decorators import login_required
#===============================================================================
# URL PATTERNS
#===============================================================================
urlpatterns = patterns('',
                       url(r'^$', login_required(IndexView.as_view()), name='index'),
                       #========================================================
                       # LINK PAGE
                       #========================================================
                       url(r'^linkpages$', login_required(LinkPageIndexView.as_view()), name='linkpage_index'),
                       url(r'^linkpages/(?P<slug>[\w-]+)$', login_required(LinkPageUpdateView.as_view()), name='linkpage_update'),
                       url(r'^linkpages/(?P<slug>[\w-]+)/delete$', login_required(LinkPageDeleteView.as_view()), name='linkpage_delete'),
                       #========================================================
                       # TEXT PAGE
                       #========================================================
                       url(r'^textpages$', login_required(TextPageIndexView.as_view()), name='textpage_index'),
                       url(r'^textpages/(?P<slug>[\w-]+)$', login_required(TextPageUpdateView.as_view()), name='textpage_update'),
                       url(r'^textpages/(?P<slug>[\w-]+)/delete$', login_required(TextPageDeleteView.as_view()), name='textpage_delete'),
                       #========================================================
                       # GALLERY PAGE
                       #========================================================
                       url(r'^gallerypages$', login_required(GalleryPageIndexView.as_view()), name='gallerypage_index'),
                       url(r'^gallerypages/(?P<slug>[\w-]+)$', login_required(GalleryPageUpdateView.as_view()), name='gallerypage_update'),
                       url(r'^gallerypages/(?P<slug>[\w-]+)/delete$', login_required(GalleryPageDeleteView.as_view()), name='gallerypage_delete'),
                       #========================================================
                       # PRODUCT PAGE
                       #========================================================
                       url(r'^productpages$', login_required(ProductPageIndexView.as_view()), name='productpage_index'),
                       url(r'^productpages/(?P<slug>[\w-]+)$', login_required(ProductPageUpdateView.as_view()), name='productpage_update'),
                       url(r'^productpages/(?P<slug>[\w-]+)/delete$', login_required(ProductPageDeleteView.as_view()), name='productpage_delete'),
                      )