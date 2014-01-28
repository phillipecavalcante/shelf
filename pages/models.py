from django.db import models
from menu.models import Menu
from timestamp.models import Timestamp

class Page(Timestamp):
    title = models.CharField(max_length=100)
    content = models.TextField()
    menuitem = models.ForeignKey(Menu)
    
    def __unicode__(self):
        return unicode(self.title)