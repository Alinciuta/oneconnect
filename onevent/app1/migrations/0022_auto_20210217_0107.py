# Generated by Django 3.1.6 on 2021-02-16 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_auto_20210217_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='eveniment',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='app1.events'),
        ),
    ]