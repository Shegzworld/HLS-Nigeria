# Generated by Django 5.0.7 on 2024-10-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0002_podcaster_podcast_podcaster'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
