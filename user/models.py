from django.db import models

from location.models import Location


class User(models.Model):
    ROLES = [('moderator', 'Модератор'), ('member', 'Пользователь'), ('admin', 'Администратор')]

    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, unique=True, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    role = models.CharField(max_length=50, blank=False, default='member', choices=ROLES)
    age = models.IntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
