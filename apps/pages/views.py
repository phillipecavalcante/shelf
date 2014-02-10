from django.views import generic
from apps.pages.models import BasicPage
from django.core.urlresolvers import reverse


class IndexView(generic.CreateView):
    
    model = BasicPage
    template_name = 'pages/index.html'
#     form_class = IndexGalleryForm
     
     
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['object_list'] = BasicPage.objects.all().order_by('-modified')
         
        return context
     
    def get_success_url(self):
        return reverse('pages:index')