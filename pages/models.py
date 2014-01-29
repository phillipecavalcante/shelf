from django.db import models
from menu.models import Menu
from timestamp.models import Timestamp

class Page(Timestamp):
    name = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    menu = models.OneToOneField(Menu, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.name)