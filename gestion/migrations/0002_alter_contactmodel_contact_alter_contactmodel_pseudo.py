# Generated by Django 4.2.1 on 2023-06-22 22:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='contact',
            field=models.IntegerField(max_length=16),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='pseudo',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
