from django.views import generic
from menu.models import Menu
from django.core.urlresolvers import reverse
from menu.forms import MenuForm

class IndexView(generic.ListView):
    template_name = 'menu/index.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return Menu.objects.all()
    
class CreateView(generic.CreateView):
    model = Menu
    template_name = 'menu/create.html'
    form_class = MenuForm
    
    def get_success_url(self):
        return reverse('menu:retrieve', kwargs={self.pk_url_kwarg: self.object.pk})


class RetrieveView(generic.DetailView):
    model = Menu
    template_name = 'menu/retrieve.html'
    
    def get_success_url(self):
        return reverse('menu:index')
            
class UpdateView(generic.edit.UpdateView):
    model = Menu
    template_name = 'menu/update.html'
    form_class = MenuForm
    
    def get_object(self, queryset=None):
        obj = Menu.objects.get(pk=self.kwargs['pk'])
        return obj
    def get_success_url(self):
        return reverse('menu:retrieve', kwargs={self.pk_url_kwarg: self.get_object().pk})
    
class DeleteView(generic.DeleteView):
    model = Menu
    template_name = 'menu/delete.html'
    
    
    def get_success_url(self):
        return reverse('menu:index')
    