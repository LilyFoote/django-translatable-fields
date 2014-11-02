from django.core.exceptions import ValidationError
from django.test import override_settings, TestCase

from translatable_fields import fields
from .models import TranslatableModel


class TestTranslatableField(TestCase):
    def test_read(self):
        name = 'Name'
        instance = TranslatableModel(name={'en': name})
        self.assertEqual(instance.name['en'], name)

    def test_save(self):
        instance = TranslatableModel()
        instance.save()

    @override_settings(LANGUAGES=(('en', 'English'), ('fr', 'French')))
    def test_allow_supported_languages(self):
        """Store translations for supported languages."""
        instance = TranslatableModel(name={'en': 'Name'})
        instance.clean_fields()

    @override_settings(LANGUAGES=(('de', 'German'), ('fr', 'French')))
    def test_disallow_unsupported_languages(self):
        """Don't Store translations for unsupported languages."""
        instance = TranslatableModel(name={'en': 'Name'})
        with self.assertRaises(ValidationError):
            instance.clean_fields()


class TestLanguageTemplate(TestCase):
    """Use the appropriate error template when validating languages."""
    def test_one_language(self):
        """Use the appropriate error template for one language."""
        template = fields.language_template(1)
        self.assertEqual(template, fields.SINGLE_LANGUAGE_TEMPLATE)

    def test_multiple_languages(self):
        """Use the appropriate error template for multiple languages."""
        template = fields.language_template(2)
        self.assertEqual(template, fields.MULTIPLE_LANGUAGE_TEMPLATE)
