# Generated by Django 3.2.18 on 2023-04-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0007_auto_20230413_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=1),
        ),
    ]
