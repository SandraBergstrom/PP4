# Generated by Django 3.2.18 on 2023-04-13 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_rename_description_recipe_c'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='c',
            new_name='description',
        ),
    ]
