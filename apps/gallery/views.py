from django.views import generic
from apps.gallery.models import Gallery
from django.core.urlresolvers import reverse
from apps.gallery.forms import IndexGalleryForm, GalleryForm
from apps.images.models import Image
from django.shortcuts import render_to_response


def search_names(request):
    if request.method == 'POST':
        search_text = request.POST["search_text"]
        
    else:
        search_text= ""

    object_list = Gallery.objects.filter(name__contains=search_text).order_by('-modified')
    
    return render_to_response('gallery/ajax_result.html', {'object_list': object_list})


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

class IndexView(generic.CreateView):
    model = Gallery
    template_name = 'gallery/index.html'
    form_class = IndexGalleryForm
     
     
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['object_list'] = Gallery.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('gallery:index')


    
#===============================================================================
# RETRIEVE AND UPDATE
#===============================================================================

class UpdateView(generic.UpdateView):
    model = Gallery
    template_name = 'gallery/update.html'
    form_class = GalleryForm
    
    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        g = Gallery.objects.get(slug=self.object.slug)
        context['object_list'] = Image.objects.filter(gallery=g).order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('gallery:index')
        #return reverse('gallery:update', kwargs={self.slug_url_kwarg: self.object.slug})

#===============================================================================
# DELETE VIEW    
#===============================================================================

class DeleteView(generic.DeleteView):
    model = Gallery
    template_name = 'gallery/delete.html'
     
     
    def get_success_url(self):
        return reverse('gallery:index')
    
