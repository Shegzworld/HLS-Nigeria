# Generated by Django 5.0.7 on 2024-10-03 22:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('health_goals', models.ManyToManyField(to='NT_gallery.healthgoal')),
                ('lifestyle', models.ManyToManyField(to='NT_gallery.lifestyle')),
                ('medical_conditions', models.ManyToManyField(to='NT_gallery.medicalcondition')),
                ('medications', models.ManyToManyField(to='NT_gallery.medication')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
