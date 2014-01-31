from django.views import generic
from django.core.urlresolvers import reverse
from products.models import Product, Gallery 

class ProductCreateView(generic.CreateView):
    model = Product
    template_name = 'products/product_create.html'
    
    def get_success_url(self):
        return reverse('products:retrieve', kwargs={self.pk_url_kwarg: self.object.pk})

class GalleryCreateView(generic.CreateView):
    model = Gallery
    template_name = 'products/gallery_create.html'
    
    def get_success_url(self):
        return reverse('products:retrieve', kwargs={self.pk_url_kwarg: self.object.pk})
    
    
class ProductRetrieveView(generic.DetailView):
    model = Product
    template_name = 'products/product_retrieve.html'
    
    def get_success_url(self):
        return reverse('products:index')
    
class GalleryRetrieveView(generic.DetailView):
    model = Product
    template_name = 'products/gallery_retrieve.html'
    
    def get_success_url(self):
        return reverse('products:index')