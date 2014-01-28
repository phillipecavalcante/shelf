from django.views import generic
from menu.models import Menu
from django.core.urlresolvers import reverse
from menu.forms import MenuForm
import json
from django.http.response import HttpResponse


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            open('arquivo.txt').write('vio ajax') 
            return self.render_to_json_response(data)
        else:
            return response





class IndexView(generic.ListView):
    template_name = 'menu/index.html'
    context_object_name = 'list'
    
    def get_queryset(self):
        return Menu.objects.all()
    
class CreateView(AjaxableResponseMixin,generic.CreateView):
    model = Menu
    template_name = 'menu/create.html'
    form_class = MenuForm
    fields = ['name', 'visible']
    
    def get_object(self, queryset=None):
        obj = Menu.objects.get(pk=self.object.pk)
        return obj
    
    def get_success_url(self):
        return reverse('menu:retrieve', kwargs={self.pk_url_kwarg: self.get_object().pk})


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
    