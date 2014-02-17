from django.db import models
from apps.menu.models import Menu
from apps.gallery.models import Gallery
from apps.timestamp.models import Timestamp, Descriptor

class AbstractPage(Timestamp, Descriptor):
    
    menu = models.OneToOneField(Menu, blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        abstract = True


class LinkPage(AbstractPage):
    pass
    
class TextPage(AbstractPage):
    content = models.TextField(blank=True, null=True)
    
    
class GalleryPage(AbstractPage):
    gallery = models.ForeignKey(Gallery)

class ProductPage(AbstractPage):
    pass