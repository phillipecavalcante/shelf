from django.db import models
from timestamp.models import Timestamp

    
class AbstractProduct(Timestamp):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    url = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        abstract = True

class Product(AbstractProduct):
#     pages = models.ForeignKey(Page) #TODO Verificar problema 
    main = models.ForeignKey('self', null=True, blank=True, related_name='related')

class Image(AbstractProduct):
    pass

class Gallery(AbstractProduct):
    images = models.ManyToManyField(Image)
