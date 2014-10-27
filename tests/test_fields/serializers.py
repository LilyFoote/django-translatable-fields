from rest_framework import serializers

from translatable_fields.serializer_fields import TranslatableField
from .models import TranslatableModel


class TranslatableSerializer(serializers.ModelSerializer):
    name = TranslatableField()

    class Meta:
        fields = ('name',)
        model = TranslatableModel
