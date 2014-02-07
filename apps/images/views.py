from django.views import generic
from apps.images.models import Image
from django.core.urlresolvers import reverse
from apps.images.forms import ImageForm
from django.views.generic.detail import SingleObjectMixin

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
    model = Image
    template_name = 'images/index.html'
    form_class = ImageForm
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['object_list'] = Image.objects.all().order_by('gallery')
        
        return context
    
    def get_success_url(self):
        return reverse('images:index')
    
#===============================================================================
# RETRIEVE AND UPDATE
#===============================================================================

class RetrieveAndUpdateView(generic.UpdateView):
    model = Image
    template_name = 'images/update.html'
    form_class = ImageForm
    
    def get_success_url(self):
        return reverse('images:update', kwargs={self.pk_url_kwarg: self.object.pk})
    
#===============================================================================
# DELETE
#===============================================================================

class DeleteView(generic.DeleteView):
    model = Image
    template_name = 'images/delete.html'
    
    
    def get_success_url(self):
        return reverse('images:create_and_list')
    
    
class ImageAddView(SingleObjectMixin, generic.FormView):
    template_name = 'books/author_detail.html'
    form_class = ImageForm
    model = Image

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ImageAddView, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('images:update', kwargs={self.pk_url_kwarg: self.object.pk})