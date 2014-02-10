"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from apps.menu.models import Menu
from apps.timestamp.models import Timestamp


class TestDescriptor(TestCase):

    
    def create_model(self):
        m = Menu.objects.create(name="Menu")
        return m
    
    def test_timestamp_unicode(self):
        m = self.create_model()
        
        self.assertTrue(issubclass(m.__class__, Timestamp),)
        self.assertEqual(m.__unicode__(), m.name)