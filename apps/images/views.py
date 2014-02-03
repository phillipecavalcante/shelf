from django.views import generic
from apps.images.models import Image
from django.core.urlresolvers import reverse
from apps.images.forms import ImageForm
from django.http.response import HttpResponseRedirect




#===============================================================================
# LIST
#===============================================================================

class ListView(generic.ListView):
    model = Image
    template_name = 'images/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['list'] = Image.objects.all()
        context['form'] = ImageForm
        return context


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

class CreateView(generic.CreateView):
    model = Image
    template_name = 'images/list.html'
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_success_url(self):
        return reverse('images:retrieve', kwargs={self.pk_url_kwarg: self.object.pk})
    
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
        return reverse('images:index')