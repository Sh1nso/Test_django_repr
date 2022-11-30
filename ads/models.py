import json

from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=50)
    is_published = models.BooleanField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
