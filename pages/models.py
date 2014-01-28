from django.db import models
from menu.models import Menu
from timestamp.models import Timestamp

class Page(Timestamp):
    title = models.CharField(max_length=100)
    content = models.TextField()
    menuitem = models.ForeignKey(Menu, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.title)
    
class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')