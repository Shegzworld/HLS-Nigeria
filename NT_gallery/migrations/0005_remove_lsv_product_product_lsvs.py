# Generated by Django 5.0.7 on 2024-11-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NT_gallery', '0004_remove_product_lsv_lsv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lsv',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='lsvs',
            field=models.ManyToManyField(related_name='products', to='NT_gallery.lsv'),
        ),
    ]
