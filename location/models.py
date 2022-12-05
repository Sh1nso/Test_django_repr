from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=20, decimal_places=6, default=0.0)
    lng = models.DecimalField(max_digits=20, decimal_places=6, default=0.0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
