from django.utils import translation
from langcodes import best_match
from rest_framework_hstore.fields import HStoreField


DEFAULT_SCORE = 90


class TranslatableField(HStoreField):
    def __init__(self, *args, fallback=None, min_score=DEFAULT_SCORE, **kwargs):
        super().__init__(*args, **kwargs)
        self.fallback = fallback
        self.min_score = min_score

    def to_native(self, value):
        translations = super().to_native(value)
        language, score = best_match(
            translation.get_language(),
            translations.keys(),
            min_score=self.min_score,
        )

        if language != 'und':
            return translations[language]
        elif self.fallback is not None:
            return translations.get(self.fallback, None)
        return None

    def from_native(self, value):
        current_language = translation.get_language()
        translations = {current_language: value}
        return super().from_native(translations)
