from django.views import generic
from apps.pages.models import *
from django.core.urlresolvers import reverse
from apps.pages.forms import *


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
    
#===============================================================================
# INDEX VIEW
#===============================================================================
    
class LinkPageIndexView(generic.CreateView):
    
    model = LinkPage
    template_name = 'pages/linkpages/index.html'
    form_class = LinkPageIndexForm
     
     
    def get_context_data(self, **kwargs):
        context = super(LinkPageIndexView, self).get_context_data(**kwargs)
        context['object_list'] = LinkPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:linkpage_index')
    

class TextPageIndexView(generic.CreateView):
    
    model = TextPage
    template_name = 'pages/textpages/index.html'
    form_class = TextPageIndexForm
     
     
    def get_context_data(self, **kwargs):
        context = super(TextPageIndexView, self).get_context_data(**kwargs)
        context['object_list'] = TextPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:textpage_index')

class GalleryPageIndexView(generic.CreateView):
    
    model = GalleryPage
    template_name = 'pages/gallerypages/index.html'
    form_class = GalleryPageIndexForm
     
     
    def get_context_data(self, **kwargs):
        context = super(GalleryPageIndexView, self).get_context_data(**kwargs)
        context['object_list'] = GalleryPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:gallerypage_index')
    
class ProductPageIndexView(generic.CreateView):
    
    model = ProductPage
    template_name = 'pages/productpages/index.html'
    form_class = ProductPageIndexForm
     
     
    def get_context_data(self, **kwargs):
        context = super(ProductPageIndexView, self).get_context_data(**kwargs)
        context['object_list'] = ProductPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:productpage_index')
    

#===============================================================================
# RETRIEVE AND UPDATE
#===============================================================================

class LinkPageUpdateView(generic.UpdateView):
    model = LinkPage
    template_name = 'pages/linkpages/update.html'
    form_class = LinkPageForm
     
    def get_success_url(self):
        return reverse('pages:linkpage_index')
    
class TextPageUpdateView(generic.UpdateView):
    model = TextPage
    template_name = 'pages/textpages/update.html'
    form_class = TextPageForm
     
    def get_success_url(self):
        return reverse('pages:textpage_index')
    
class GalleryPageUpdateView(generic.UpdateView):
    model = GalleryPage
    template_name = 'pages/gallerypages/update.html'
    form_class = GalleryPageForm
     
    def get_success_url(self):
        return reverse('pages:gallerypage_index')
    
class ProductPageUpdateView(generic.UpdateView):
    model = ProductPage
    template_name = 'pages/productpages/update.html'
    form_class = ProductPageForm
     
    def get_success_url(self):
        return reverse('pages:productpage_index')
        
        
      
#===============================================================================
# DELETE
#===============================================================================

class LinkPageDeleteView(generic.DeleteView):
    model = LinkPage
    template_name = 'pages/linkpages/delete.html'
     
     
    def get_success_url(self):
        return reverse('pages:linkpage_index')
    
class TextPageDeleteView(generic.DeleteView):
    model = TextPage
    template_name = 'pages/textpages/delete.html'
     
     
    def get_success_url(self):
        return reverse('pages:textpage_index')
    
class GalleryPageDeleteView(generic.DeleteView):
    model = GalleryPage
    template_name = 'pages/gallerypages/delete.html'
     
     
    def get_success_url(self):
        return reverse('pages:gallerypage_index')
    
class ProductPageDeleteView(generic.DeleteView):
    model = ProductPage
    template_name = 'pages/productpages/delete.html'
     
     
    def get_success_url(self):
        return reverse('pages:productpage_index')
