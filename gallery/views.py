from django.views import generic
from gallery.models import Image, Gallery
from django.core.urlresolvers import reverse



#===============================================================================
# LIST VIEWS
#===============================================================================

class ImageCreateView(generic.CreateView):
    model = Image
    template_name = 'gallery/image_create.html'
    
    def get_success_url(self):
        return reverse('gallery:image_create')
    
    
class ImageRetrieveView(generic.DetailView):
    model = Image
    template_name = 'gallery/list.html'
    
    def get_success_url(self):
        return reverse('gallery:gallery_create')
    
    
class GalleryCreateView(generic.CreateView):
    model = Gallery
    template_name = 'gallery/gallery_create.html'
    
    def get_success_url(self):
        return reverse('gallery:image_create')
    
    
class GalleryRetrieveView(generic.DetailView):
    model = Gallery
    template_name = 'gallery/create.html'
    
    def get_success_url(self):
        return reverse('gallery:create.html', kwargs={self.pk_url_kwarg: self.object.pk})