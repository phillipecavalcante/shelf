from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from timestamp.models import Timestamp

class Menu(MPTTModel, Timestamp):
    
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    name = models.CharField(max_length=30, unique=True, blank=False, null=False)
    position = models.PositiveSmallIntegerField(unique=True, default=0, blank=False, null=False)
    public = models.BooleanField(default=False, blank=False, null=False)
    
    def __unicode__(self):
        return self.name
    
    def is_public(self):
        return self.public
    
    class MPTTMeta:
        order_insertion_by = ['name']