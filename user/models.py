from django.contrib.auth.models import AbstractUser
from django.db import models

from location.models import Location


class User(AbstractUser):
    ROLES = [('moderator', 'Модератор'), ('member', 'Пользователь'), ('admin', 'Администратор')]

    role = models.CharField(max_length=50, blank=False, default='member', choices=ROLES)
    age = models.IntegerField()
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

