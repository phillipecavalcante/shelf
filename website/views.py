# from django.views import generic
# from menu.models import Menu
# # from pages.models import Page
# from django.core.urlresolvers import reverse
# 
# class IndexView(generic.ListView):
#     template_name = 'website/base2.html'
#     context_object_name = 'list'
#     
#     def get_queryset(self):
#         return Menu.objects.all()
# 
# class DetailView(generic.DetailView):
#     template_name = 'website/page.html'
#     model = Page
#     
#     def get_object(self, queryset=None):
#         obj = Page.objects.get(pk=self.kwargs['pk'])
#         return obj
#     
#     def get_success_url(self):
#         return reverse('website:index', kwargs={self.pk_url_kwarg: self.get_object().pk})
#     