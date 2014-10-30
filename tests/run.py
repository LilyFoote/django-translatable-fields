#! /usr/bin/env python
"""From http://stackoverflow.com/a/12260597/400691"""
import sys

from colour_runner.django_runner import ColourRunnerMixin
import django
from django.conf import settings
from django.test.runner import DiscoverRunner
import dj_database_url


settings.configure(
    DATABASES={
        'default': dj_database_url.config(
            default='postgres://localhost/translatable_fields',
        ),
    },
    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    INSTALLED_APPS=(),
    MIDDLEWARE_CLASSES=(),
)

django.setup()


class TestRunner(ColourRunnerMixin, DiscoverRunner):
    pass


test_runner = TestRunner(verbosity=1)
failures = test_runner.run_tests(['tests'])
if failures:
    sys.exit(1)
