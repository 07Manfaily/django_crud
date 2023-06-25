# Generated by Django 4.2.1 on 2023-06-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')], max_length=100)),
                ('contact', models.CharField(max_length=100)),
            ],
        ),
    ]