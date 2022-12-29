from django.core.exceptions import ValidationError


def check_length_of_slug(value: str):
    if len(value) < 5 or len(value) > 10:
        raise ValidationError(f"{value} does not match")
