# Generated by Django 3.2.18 on 2023-04-17 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0017_alter_recipe_featured_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='member',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
