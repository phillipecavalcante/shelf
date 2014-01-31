from django.db import models
from imagekit.models import ImageSpecField
from apps.timestamp.models import Timestamp, Descriptor
from pilkit.processors.resize import SmartResize


class Gallery(Timestamp, Descriptor):
    pass
    
class Image(Timestamp, Descriptor):
    image = models.FileField(upload_to='images/%Y/%m%d')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[SmartResize(100,50, True)],
                                     format='JPEG',
                                     options={'quality':100})
    
    gallery = models.ManyToManyField(Gallery, blank=True, null=True)
    
    def __unicode__(self):
        return self.name