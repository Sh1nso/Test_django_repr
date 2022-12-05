from django.db import models

from category.models import Category
from user.models import User


class Ads(models.Model):
    name = models.CharField(max_length=50)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=500)
    is_published = models.BooleanField(blank=True)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
