# Generated by Django 5.0.7 on 2024-11-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NT_gallery', '0002_maincategory_category_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='lsvs',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='NT_gallery.lsv'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pictures',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='strength',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_categories',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
