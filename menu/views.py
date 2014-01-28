from django.views import generic
from menu.models import Menu

class IndexView(generic.ListView):
    template_name = 'menu/index.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return Menu.objects.all()
    
class CreateView(generic.edit.CreateView):
    model = Menu
    fields = ['name']
    template_name = 'menu/create.html'
    success_url = '/menu/'


class RetrieveView(generic.DetailView):
    model = Menu
    template_name = 'menu/retrieve.html'
            
class UpdateView(generic.edit.UpdateView):
    model = Menu
    fields = ['name']
    template_name = 'menu/update.html'
    success_url = '/menu/'
    
class DeleteView(generic.edit.DeleteView):
    model = Menu
    template_name = 'menu/delete.html'
    success_url = '/menu/'