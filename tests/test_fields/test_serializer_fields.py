from django.test import TestCase, override_settings

from . import serializers
from .models import TranslatableModel


class TestTranslatableField(TestCase):
    def setUp(self):
        self.english_name = 'Name'
        self.brazilian_name = 'Nome'
        translated_names = {
            'en': self.english_name,
            'pt-br': self.brazilian_name,
        }

        self.instance = TranslatableModel(name=translated_names)
        self.serializer = serializers.TranslatableSerializer(self.instance)

    @override_settings(LANGUAGE_CODE='en')
    def test_serialize_english(self):
        expected_data = {'name': self.english_name}
        self.assertEqual(self.serializer.data, expected_data)

    @override_settings(LANGUAGE_CODE='en-gb')
    def test_serialize_english_gb(self):
        expected_data = {'name': self.english_name}
        self.assertEqual(self.serializer.data, expected_data)

    @override_settings(LANGUAGE_CODE='pt-br')
    def test_serialize_brazilian_portuguese(self):
        expected_data = {'name': self.brazilian_name}
        self.assertEqual(self.serializer.data, expected_data)

    @override_settings(LANGUAGE_CODE='pt')
    def test_serialize_portuguese(self):
        expected_data = {'name': self.brazilian_name}
        self.assertEqual(self.serializer.data, expected_data)

    @override_settings(LANGUAGE_CODE='de')
    def test_serialize_german(self):
        expected_data = {'name': None}
        self.assertEqual(self.serializer.data, expected_data)

    @override_settings(LANGUAGE_CODE='de')
    def test_serialize_german_fallback_to_english(self):
        serializer = serializers.FallbackSerializer(self.instance)

        expected_data = {'name': self.english_name}
        self.assertEqual(serializer.data, expected_data)

    @override_settings(LANGUAGE_CODE='de')
    def test_serialize_german_fallback_to_missing_english(self):
        translated_names = {'pt-br': self.brazilian_name}
        instance = TranslatableModel(name=translated_names)
        serializer = serializers.FallbackSerializer(instance)

        expected_data = {'name': None}
        self.assertEqual(serializer.data, expected_data)
