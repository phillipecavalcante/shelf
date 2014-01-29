from django.db import models
from menu.models import Menu
from timestamp.models import Timestamp
from products.models import Gallery, Product

class AbstractPage(Timestamp):
    name = models.CharField(max_length=50, blank=False, null=False)
    menu = models.OneToOneField(Menu, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.name)
    
    class Meta:
        abstract = True


class LinkPage(AbstractPage):
    url = models.URLField(blank=True)
    
class BasicPage(AbstractPage):
    content = models.TextField(blank=True)
    
    
class GalleryPage(AbstractPage):
    content = models.ForeignKey(Gallery)

class ProductPage(AbstractPage):
    content = models.ForeignKey(Product)