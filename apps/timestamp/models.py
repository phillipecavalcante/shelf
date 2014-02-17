from django.db import models
from autoslug.fields import AutoSlugField


class Descriptor(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(default='', blank=True)
    url = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        abstract = True
        
class Timestamp(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)
    
    class Meta:
        abstract = True