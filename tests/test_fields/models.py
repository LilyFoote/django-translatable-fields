from django.db import models

from translatable_fields.fields import TranslatableField


class TranslatableModel(models.Model):
    name = TranslatableField()
