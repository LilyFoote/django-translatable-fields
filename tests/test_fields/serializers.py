from rest_framework import serializers

from translatable_fields.serializer_fields import TranslatableField
from .models import TranslatableModel


class TranslatableMeta:
    fields = ('name',)
    model = TranslatableModel


class TranslatableSerializer(serializers.ModelSerializer):
    name = TranslatableField()

    Meta = TranslatableMeta


class FallbackSerializer(serializers.ModelSerializer):
    name = TranslatableField(fallback='en')

    Meta = TranslatableMeta


class StrictSerializer(serializers.ModelSerializer):
    name = TranslatableField(min_score=100)

    Meta = TranslatableMeta
