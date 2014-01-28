from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from timestamp.models import Timestamp

class Menu(MPTTModel, Timestamp):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    visible = models.BooleanField()
    
    def __unicode__(self):
        return self.name
    
    def is_visible(self):
        return self.visible
    is_visible.boolean = True
    is_visible.short_description = 'Is visible?'
    
    class MPTTMeta:
        order_insertion_by = ['name']