# Generated by Django 5.0.7 on 2024-10-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NT_gallery', '0011_remove_product_lifestyle_rating_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifestyleRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LifestyleRating', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
