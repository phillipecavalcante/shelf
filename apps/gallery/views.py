from django.views import generic
from apps.gallery.models import Gallery, Image
from django.core.urlresolvers import reverse
from apps.gallery.forms import GalleryForm, ImageForm



#===============================================================================
# LIST VIEW
#===============================================================================

class GalleryList(generic.ListView):
    model = Gallery
    template_name = 'gallery/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(GalleryList, self).get_context_data(**kwargs)
        context['list'] = Gallery.objects.all()
        context['form'] = GalleryForm()
        return context

#===============================================================================
# CREATE VIEW
#===============================================================================

class GalleryCreate(generic.CreateView):
    model = Gallery
    template_name = 'gallery/create.html'
    form_class = GalleryForm
    
    
    def get_success_url(self):
        return reverse('gallery:index')

#===============================================================================
# RETRIEVE VIEW
#===============================================================================

class GalleryRetrieve(generic.DetailView):
    model = Gallery
    template_name = 'gallery/retrieve.html'
    
    def get_context_data(self, **kwargs):
        context = super(GalleryRetrieve, self).get_context_data(**kwargs)
        context['list'] = Image.objects.filter(gallery=Gallery.objects.get(pk=self.object.pk))
        context['form'] = ImageForm
        return context
    
    def get_success_url(self):
        return reverse('gallery:index')
    
#===============================================================================
# UPDATE VIEW
#===============================================================================

class GalleryUpdate(generic.UpdateView):
    model = Gallery
    template_name = 'gallery/update.html'
    
    def get_success_url(self):
        return reverse('gallery:retrieve', kwargs={self.pk_url_kwarg: self.object.pk})

#===============================================================================
# DELETE VIEW    
#===============================================================================

class GalleryDelete(generic.DeleteView):
    model = Gallery
    template_name = 'gallery/delete.html'
    
    
    def get_success_url(self):
        return reverse('gallery:index')

class ImageCreateView(generic.CreateView):
    model = Image
    template_name = 'gallery/image_create.html'
     
    def get_success_url(self):
        return reverse('gallery:image_create')
#     
#     
# class ImageRetrieveView(generic.DetailView):
#     model = Image
#     template_name = 'gallery/list.html'
#     
#     def get_success_url(self):
#         return reverse('gallery:gallery_create')
#         
#     
# class GalleryRetrieveView(generic.DetailView):
#     model = Gallery
#     template_name = 'gallery/create.html'
#     
#     def get_success_url(self):
#         return reverse('gallery:create.html', kwargs={self.pk_url_kwarg: self.object.pk})