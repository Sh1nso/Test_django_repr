# Generated by Django 4.1.4 on 2022-12-29 13:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True, validators=[django.core.validators.MinValueValidator(5)]),
        ),
    ]
