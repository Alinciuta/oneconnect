# Generated by Django 3.1.6 on 2021-02-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=200, unique=True)),
                ('banner', models.ImageField(blank=True, null=True, upload_to='bannere')),
                ('eventdate', models.CharField(max_length=200)),
                ('eventdescription', models.TextField(default='')),
                ('eventagenda', models.TextField(default='')),
                ('event_type', models.CharField(choices=[('Virtual', 'Virtual'), ('Live', 'Live'), ('Hybrid', 'Hybrid')], max_length=50)),
                ('video_url', models.CharField(max_length=1000, null=True, unique=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
    ]
