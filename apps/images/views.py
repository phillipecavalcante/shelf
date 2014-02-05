from django.views import generic
from apps.images.models import Image
from django.core.urlresolvers import reverse
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
# CREATE
#===============================================================================

class CreateAndListView(generic.CreateView):
    model = Image
    template_name = 'images/list.html'
    form_class = ImageForm
    
    def get_context_data(self, **kwargs):
        context = super(CreateAndListView, self).get_context_data(**kwargs)
        context['list'] = Image.objects.all()
        
        return context
    
    def get_success_url(self):
        return reverse('images:create_and_list')
    
#===============================================================================
# RETRIEVE
#===============================================================================

class RetrieveView(generic.DetailView):
    model = Image
    template_name = 'images/retrieve.html'
    
    def get_success_url(self):
        return reverse('images:retrieve', kwargs={self.pk_url_kwarg: self.object.pk})
    
#===============================================================================
# UPDATE
#===============================================================================

class UpdateView(generic.UpdateView):
    model = Image
    template_name = 'images/update.html'
    
    def get_success_url(self):
        return reverse('images:retrieve', kwargs={self.pk_url_kwarg: self.object.pk})
    
#===============================================================================
# DELETE
#===============================================================================

class DeleteView(generic.DeleteView):
    model = Image
    template_name = 'images/delete.html'
    
    def get_success_url(self):
        return reverse('images:list')