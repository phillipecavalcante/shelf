from django.contrib.auth import logout
from django.core.urlresolvers import reverse

def logout_view(request):
    logout(request)
    return reverse('dashboard:index')