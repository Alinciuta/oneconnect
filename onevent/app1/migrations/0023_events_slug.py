# Generated by Django 3.1.6 on 2021-02-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_auto_20210217_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='slug',
            field=models.SlugField(default=1, max_length=100, unique=True),
        ),
    ]