from django.views import generic
from apps.pages.models import LinkPage, TextPage, GalleryPage, ProductPage
from django.core.urlresolvers import reverse
from apps.pages.forms import LinkPageIndexForm, TextPageIndexForm, GalleryPageIndexForm, ProductPageIndexForm


class IndexView(generic.CreateView):
    
    model = TextPage
    template_name = 'pages/index.html'
#     form_class = IndexGalleryForm
     
     
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['object_list'] = TextPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:index')
    
    
class LinkPageIndexView(generic.CreateView):
    
    model = LinkPage
    template_name = 'pages/linkpage_index.html'
    form_class = LinkPageIndexForm
     
     
    def get_context_data(self, **kwargs):
        context = super(LinkPageIndexView, self).get_context_data(**kwargs)
        context['object_list'] = LinkPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:linkpage_index')
    

class TextPageIndexView(generic.CreateView):
    
    model = TextPage
    template_name = 'pages/textpage_index.html'
    form_class = TextPageIndexForm
     
     
    def get_context_data(self, **kwargs):
        context = super(TextPageIndexView, self).get_context_data(**kwargs)
        context['object_list'] = TextPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:textpage_index')

class GalleryPageIndexView(generic.CreateView):
    
    model = GalleryPage
    template_name = 'pages/gallerypage_index.html'
    form_class = GalleryPageIndexForm
     
     
    def get_context_data(self, **kwargs):
        context = super(GalleryPageIndexView, self).get_context_data(**kwargs)
        context['object_list'] = GalleryPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:gallerypage_index')
    
class ProductPageIndexView(generic.CreateView):
    
    model = ProductPage
    template_name = 'pages/productpage_index.html'
    form_class = ProductPageIndexForm
     
     
    def get_context_data(self, **kwargs):
        context = super(ProductPageIndexView, self).get_context_data(**kwargs)
        context['object_list'] = ProductPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:productpage_index')