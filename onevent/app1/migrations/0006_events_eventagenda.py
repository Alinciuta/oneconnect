# Generated by Django 3.1.6 on 2021-02-13 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210211_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='eventagenda',
            field=models.TextField(default='Event Agenda'),
        ),
    ]