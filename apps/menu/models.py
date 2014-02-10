from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from apps.timestamp.models import Timestamp, Descriptor

class Menu(MPTTModel, Timestamp, Descriptor):
    
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
        
    class MPTTMeta:
        order_insertion_by = ['name']