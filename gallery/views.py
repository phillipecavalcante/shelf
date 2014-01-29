from django.views import generic
from gallery.models import Gallery
from django.core.urlresolvers import reverse


#===============================================================================
# LIST VIEWS
#===============================================================================

class GalleryList(generic.ListView):
    template_name = 'gallery/list.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return Gallery.objects.all()
    
class GalleryCreate(generic.CreateView):
    model = Gallery
    fields = ['name']
    template_name = 'gallery/list.html'
    
    def get_success_url(self):
        return reverse('gallery:list')