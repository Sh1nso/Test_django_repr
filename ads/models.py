from django.db import models
from django.http import JsonResponse

from category.models import Category
from user.models import User


class Ads(models.Model):
    name = models.CharField(max_length=50)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=500)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/', default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def author(self):
        return self.author_id.first_name + ' ' + self.author_id.last_name if self.author_id else None

    def ads_category(self):
        return self.category.name if self.category else None


class AdsCompilation(models.Model):
    name = models.CharField(max_length=500)
    items = models.ManyToManyField(Ads)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def owner(self):
        return self.owner_id.username if self.owner_id else None
