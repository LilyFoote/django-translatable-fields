from django.test import TestCase

from .models import TranslatableModel


class TestTranslatableField(TestCase):
    def test_read(self):
        name = 'Name'
        instance = TranslatableModel(name={'en': name})
        self.assertEqual(instance.name['en'], name)

    def test_save(self):
        instance = TranslatableModel()
        instance.save()
