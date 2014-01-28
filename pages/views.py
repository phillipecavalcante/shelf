from django.views import generic
from pages.models import Page
from pages.forms import PageForm
from django.core.urlresolvers import reverse

class IndexView(generic.ListView):
    template_name = 'pages/index.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return Page.objects.all()
    
class CreateView(generic.CreateView):
    model = Page
    #fields = ['title', 'content']
    template_name = 'pages/create.html'
    form_class = PageForm
 
    def get_success_url(self):
        return reverse('pages:index')
    
class RetrieveView(generic.DetailView):
    model = Page
    template_name = 'pages/retrieve.html'
    
    def get_success_url(self):
        return reverse('pages:index')
    
class UpdateView(generic.UpdateView):
    model = Page
    #fields = ['title', 'content']
    template_name = 'pages/update.html'
    form_class = PageForm
    
    def get_object(self, queryset=None):
        obj = Page.objects.get(pk=self.kwargs['pk'])
        return obj

    def get_success_url(self):
        
        return reverse('pages:retrieve', kwargs={self.pk_url_kwarg: self.get_object().pk})
    
class DeleteView(generic.DeleteView):
    model = Page
    template_name = 'pages/delete.html'
    success_url = '/pages/'
    
