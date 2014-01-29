from django.views import generic
from pages.models import BasicPage, LinkPage , GalleryPage, ProductPage
from django.core.urlresolvers import reverse


#===============================================================================
# LIST VIEWS
#===============================================================================

class ListViewBasicPage(generic.ListView):
    template_name = 'pages/basicpage_list.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return BasicPage.objects.all()
    
class ListViewLinkPage(generic.ListView):
    template_name = 'pages/linkpage_list.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return LinkPage.objects.all()

class ListViewGalleryPage(generic.ListView):
    template_name = 'pages/gallerypage_list.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return GalleryPage.objects.all()

class ListViewProductPage(generic.ListView):
    template_name = 'pages/productpage_list.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return ProductPage.objects.all()

#===============================================================================
# CREATE VIEWS
#===============================================================================

class CreateViewLinkPage(generic.CreateView):
    model = LinkPage
    template_name = 'pages/linkpage_create.html'
 
    def get_success_url(self):
        return reverse('pages:linkpage_list')
    
class CreateViewBasicPage(generic.CreateView):
    model = BasicPage
    template_name = 'pages/basicpage_create.html'
 
    def get_success_url(self):
        return reverse('pages:basicpage_list')

class CreateViewGalleryPage(generic.CreateView):
    model = GalleryPage
    #fields = ['title', 'content']
    template_name = 'pages/gallerypage_create.html'
 
    def get_success_url(self):
        return reverse('pages:gallerypage_list')
    
class CreateViewProductPage(generic.CreateView):
    model = ProductPage
    #fields = ['title', 'content']
    template_name = 'pages/productpage_create.html'
 
    def get_success_url(self):
        return reverse('pages:productpage_list')
# class RetrieveView(generic.DetailView):
#     model = Page
#     template_name = 'pages/retrieve.html'
#     
#     def get_success_url(self):
#         return reverse('pages:index')
#     
# class UpdateView(generic.UpdateView):
#     model = Page
#     #fields = ['title', 'content']
#     template_name = 'pages/update.html'
#     form_class = PageForm
#     
#     def get_object(self, queryset=None):
#         obj = Page.objects.get(pk=self.kwargs['pk'])
#         return obj
# 
#     def get_success_url(self):
#         
#         return reverse('pages:retrieve', kwargs={self.pk_url_kwarg: self.get_object().pk})
#     
# class DeleteView(generic.DeleteView):
#     model = Page
#     template_name = 'pages/delete.html'
#     success_url = '/pages/'
#     
