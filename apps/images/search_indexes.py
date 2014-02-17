import datetime
from haystack import indexes
from apps.images.models import Image


class ImageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    slug = indexes.CharField(model_attr='slug')
    description = indexes.CharField(model_attr='description')
    created = indexes.DateTimeField(model_attr='created')
    modified = indexes.DateTimeField(model_attr='modified')

    def get_model(self):
        return Image

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(modified__lte=datetime.datetime.now())