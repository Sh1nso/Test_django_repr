from django.core.exceptions import ValidationError
from django.db import models


def check_length_of_slug(value: str):
    if len(value) < 5 or len(value) > 10:
        raise ValidationError(f"{value} does not match")


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, null=True, validators=[check_length_of_slug])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
