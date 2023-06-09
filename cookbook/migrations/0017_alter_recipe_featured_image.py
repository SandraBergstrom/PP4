# Generated by Django 3.2.18 on 2023-04-16 11:00

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0016_recipe_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
