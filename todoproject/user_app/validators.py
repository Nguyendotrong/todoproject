
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodePhoneValidator(validators.RegexValidator):
    regex = r"0\d{9}"
    message = _(
        'Enter a valid phone. This value may contain number, exactly 10 numbers'
    )
    flags = 0

