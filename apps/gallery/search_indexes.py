from haystack import indexes
from apps.gallery.models import Gallery


class GalleryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    slug = indexes.CharField(model_attr='slug')
    description = indexes.CharField(model_attr='description')
    created = indexes.DateTimeField(model_attr='created')
    modified = indexes.DateTimeField(model_attr='modified')
    
    def get_model(self):
        return Gallery

    def index_queryset(self, using=None):
        return self.get_model().objects.all()