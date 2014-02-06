from django.views import generic
from apps.gallery.models import Gallery
from apps.images.models import Image
from django.core.urlresolvers import reverse
from apps.gallery.forms import GalleryForm
from apps.images.forms import ImageForm


#===============================================================================
# 
#===============================================================================
#===============================================================================
# CRUD
#===============================================================================
#===============================================================================
# 
#===============================================================================



#===============================================================================
# CREATE AND LIST
#===============================================================================

class CreateAndListView(generic.CreateView):
    model = Gallery
    template_name = 'gallery/create_and_list.html'
    form_class = GalleryForm
    
    
    def get_context_data(self, **kwargs):
        context = super(CreateAndListView, self).get_context_data(**kwargs)
        context['list'] = Gallery.objects.all()
        
        return context
    
    def get_success_url(self):
        return reverse('gallery:create_and_list')



    
#===============================================================================
# UPDATE AND CREATE IMAGE VIEW
#===============================================================================

class CreateAndListImageView(generic.DetailView):
    model = Gallery
    template_name = 'gallery/create_and_list_images.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(CreateAndListImageView, self).get_context_data(**kwargs)
        context['list'] = Image.objects.filter(gallery=Gallery.objects.get(slug=self.object.slug))
        context['form'] = ImageForm
        
        return context
        
    def get_success_url(self):
        
        return reverse('gallery:create_and_list_images', kwargs={self.slug_url_kwarg: self.object.slug})

#===============================================================================
# DELETE VIEW    
#===============================================================================

class GalleryDelete(generic.DeleteView):
    model = Gallery
    template_name = 'gallery/delete.html'
    
    
    def get_success_url(self):
        return reverse('gallery:create_and_list')
    
