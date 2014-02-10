from django.views import generic
from apps.menu.models import Menu
from django.core.urlresolvers import reverse
from apps.menu.forms import MenuIndexForm, MenuForm

class IndexView(generic.CreateView):
    model = Menu
    template_name = 'menu/index.html'
    form_class = MenuIndexForm
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['nodes'] = Menu.objects.all()
        
        return context
    
    def get_success_url(self):
        return reverse('menu:index')
    
#===============================================================================
# RETRIEVE AND UPDATE
#===============================================================================

class UpdateView(generic.UpdateView):
    model = Menu
    template_name = 'menu/update.html'
    form_class = MenuForm
     
    def get_success_url(self):
        return reverse('menu:index')
        #return reverse('images:update', kwargs={self.slug_url_kwarg: self.object.slug})
    
#===============================================================================
# DELETE
#===============================================================================

class DeleteView(generic.DeleteView):
    model = Menu
    template_name = 'menu/delete.html'
     
     
    def get_success_url(self):
        return reverse('menu:index')
