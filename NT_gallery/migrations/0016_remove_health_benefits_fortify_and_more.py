# Generated by Django 5.0.7 on 2024-10-31 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NT_gallery', '0015_health_benefits_name'),
    ]

    operations = [
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
            name='health_support',
        ),
        migrations.AddField(
            model_name='health_benefits',
            name='Fortify',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_benefits', to='NT_gallery.fortify'),
        ),
        migrations.AddField(
            model_name='health_benefits',
            name='Side_effects',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_benefits', to='NT_gallery.side_effects'),
        ),
        migrations.AddField(
            model_name='health_benefits',
            name='health_support',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='health_benefits', to='NT_gallery.health_support'),
        ),
    ]
