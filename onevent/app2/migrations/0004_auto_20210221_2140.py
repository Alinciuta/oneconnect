# Generated by Django 3.1.6 on 2021-02-21 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
        ('app2', '0003_auto_20210220_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='eveniment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_questions', to='app1.events'),
        ),
    ]