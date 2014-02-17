from django.views import generic
from apps.menu.models import Menu
from django.core.urlresolvers import reverse
from apps.pages.models import LinkPage, TextPage, GalleryPage, ProductPage
 
class IndexView(generic.ListView):
    template_name = 'website/base2.html'
    context_object_name = 'list'
     
    def get_queryset(self):
        return Menu.objects.all()

#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         context['linkpages'] = LinkPage.objects.all().order_by('-modified')
#         context['textpages'] = TextPage.objects.all().order_by('-modified')
#         context['gallerypages'] = GalleryPage.objects.all().order_by('-modified')
#         context['productpages'] = ProductPage.objects.all().order_by('-modified')
#         
#         return context
#     
    
class TextPageDetailView(generic.DetailView):
    template_name = 'website/page.html'
    model = TextPage

    def get_context_data(self, **kwargs):
        context = super(TextPageDetailView, self).get_context_data(**kwargs)
        context['list'] = Menu.objects.all()
         
        return context
#     
#     
#     def get_success_url(self):
#         return reverse('website:index', kwargs={self.pk_url_kwarg: self.get_object().pk})