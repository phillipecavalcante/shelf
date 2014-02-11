from django.views import generic

class IndexView(generic.ListView):
    template_name = 'dashboard/index.html'
    queryset = []