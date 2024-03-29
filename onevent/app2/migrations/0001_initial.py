# Generated by Django 3.1.6 on 2021-02-17 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('eveniment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='app1.events')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
