# Generated by Django 5.0.7 on 2024-11-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NT_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mlv',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
