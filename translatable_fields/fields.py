from django.conf import settings
from django.core.exceptions import ValidationError
from django_hstore import hstore


SINGLE_LANGUAGE_TEMPLATE = 'Language "{}" is not available.'
MULTIPLE_LANGUAGE_TEMPLATE = 'Languages "{}" are not available.'


def language_template(count):
    """Select the correct template for the given count."""
    if count == 1:
        return SINGLE_LANGUAGE_TEMPLATE
    return MULTIPLE_LANGUAGE_TEMPLATE


def validate_languages(value):
    """Restrict the allowed languages to those in setings.LANGUAGES."""
    allowed_languages = {lang for lang, display in settings.LANGUAGES}
    languages = value.keys()
    if languages <= allowed_languages:
        return

    disallowed_languages = languages - allowed_languages
    template = language_template(len(disallowed_languages))
    message = template.format(', '.join(disallowed_languages))
    raise ValidationError(message)


class TranslatableField(hstore.DictionaryField):
    default_validators = [validate_languages]
