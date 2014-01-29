from django.db import models
from timestamp.models import Timestamp

    
class Image(Timestamp):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    url = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.name

class Gallery(Timestamp):
    name = models.CharField(max_length=30)
    images = models.ManyToManyField(Image)
    
# class Product(AbstractProduct):
# #     pages = models.ForeignKey(Page) #TODO Verificar problema 
#     main = models.ForeignKey('self', null=True, blank=True, related_name='related')
# 
# 
# class Gallery(AbstractProduct):
#     images = models.ManyToManyField(Image)
