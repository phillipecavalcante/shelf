from django.db import models
from apps.timestamp.models import Timestamp, Descriptor
from imagekit.models.fields import ImageSpecField
from apps.gallery.models import Gallery
from pilkit.processors.resize import SmartResize

class Image(Timestamp, Descriptor):
    image = models.FileField(upload_to='images/%Y/%m/%d')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[SmartResize(100,100, True)],
                                     format='JPEG',
                                     options={'quality':100})
    
    gallery = models.ForeignKey(Gallery, blank=True, null=True)