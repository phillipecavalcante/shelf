#===============================================================================
# DJANGO
#===============================================================================
from django.views import generic
from django.core.urlresolvers import reverse
#===============================================================================
# APPS
#===============================================================================
from apps.images.models import Image
from apps.images.forms import *

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
# INDEX VIEW
#===============================================================================

class IndexView(generic.CreateView):
    model = Image
    template_name = 'images/index.html'
    form_class = ImageIndexForm
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['object_list'] = Image.objects.all().order_by('-modified')
        
        return context
    
    def get_success_url(self):
        return reverse('images:index')
    
#===============================================================================
# RETRIEVE AND UPDATE
#===============================================================================

class UpdateView(generic.UpdateView):
    model = Image
    template_name = 'images/update.html'
    form_class = ImageForm
    
    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['object'] = Image.objects.get(slug=self.object.slug)
        
        return context
    
    def get_success_url(self):
        return reverse('images:update', kwargs={self.slug_url_kwarg: self.object.slug})
    
#===============================================================================
# DELETE
#===============================================================================

class DeleteView(generic.DeleteView):
    model = Image
    template_name = 'images/delete.html'
     
     
    def get_success_url(self):
        return reverse('images:index')
