from django.db import models
from imagekit.models import ImageSpecField
from apps.timestamp.models import Timestamp, Descriptor
from pilkit.processors.resize import SmartResize


class Gallery(Timestamp, Descriptor):
    pass
