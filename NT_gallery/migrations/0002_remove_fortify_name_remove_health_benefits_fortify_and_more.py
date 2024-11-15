# Generated by Django 5.0.7 on 2024-11-15 00:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NT_gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fortify',
            name='name',
        ),
        migrations.RemoveField(
            model_name='health_benefits',
            name='Fortify',
        ),
        migrations.RemoveField(
            model_name='health_benefits',
            name='Side_effects',
        ),
        migrations.RemoveField(
            model_name='health_benefits',
            name='name',
        ),
        migrations.RemoveField(
            model_name='health_support',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fortify',
        ),
        migrations.RemoveField(
            model_name='product',
            name='health_support',
        ),
        migrations.RemoveField(
            model_name='product',
            name='side_effect',
        ),
        migrations.RemoveField(
            model_name='side_effects',
            name='name',
        ),
        migrations.AddField(
            model_name='fortify',
            name='nutrient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NT_gallery.product'),
        ),
        migrations.AddField(
            model_name='health_benefits',
            name='side_effect',
            field=models.ManyToManyField(blank=True, related_name='products', to='NT_gallery.side_effects'),
        ),
        migrations.AddField(
            model_name='health_support',
            name='nutrient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NT_gallery.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='health_benefit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='NT_gallery.health_benefits'),
        ),
        migrations.AddField(
            model_name='side_effects',
            name='nutrient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NT_gallery.product'),
        ),
        migrations.RemoveField(
            model_name='health_benefits',
            name='health_support',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_categories',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AddField(
            model_name='health_benefits',
            name='fortify',
            field=models.ManyToManyField(blank=True, related_name='products', to='NT_gallery.fortify'),
        ),
        migrations.AddField(
            model_name='health_benefits',
            name='health_support',
            field=models.ManyToManyField(blank=True, related_name='products', to='NT_gallery.health_support'),
        ),
    ]
