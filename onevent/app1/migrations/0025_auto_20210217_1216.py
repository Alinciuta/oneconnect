# Generated by Django 3.1.6 on 2021-02-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0024_auto_20210217_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='slug',
            field=models.SlugField(default='', max_length=100, unique=True),
        ),
    ]