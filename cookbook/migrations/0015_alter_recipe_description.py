# Generated by Django 3.2.18 on 2023-04-13 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0014_recipe_excerp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]