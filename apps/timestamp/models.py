from django.db import models


class Descriptor(models.Model):
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.name)
    
    class Meta:
        abstract = True
        
class Timestamp(models.Model):
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True