import datetime
from haystack import indexes
from apps.images.models import Image


class ImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    

    def get_model(self):
        return Image

    def image_queryset(self, using=None):
        return self.get_model().objects.filter(modified__lte=datetime.datetime.now())