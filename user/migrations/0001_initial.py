# Generated by Django 5.0.7 on 2024-11-09 11:15

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_form', models.CharField(blank=True, max_length=20, null=True)),
                ('health_budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Lifestyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habits', models.CharField(blank=True, max_length=255, null=True)),
                ('recreation', models.CharField(blank=True, max_length=255, null=True)),
                ('lifestyle', models.CharField(blank=True, max_length=255, null=True)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lifestyle', to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='HealthCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_complaints', models.CharField(blank=True, max_length=255, null=True)),
                ('current_medications', models.CharField(blank=True, max_length=255, null=True)),
                ('genetic_history', models.CharField(blank=True, max_length=255, null=True)),
                ('allergies', models.CharField(blank=True, max_length=255, null=True)),
                ('health_fears', models.TextField(blank=True, null=True)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='health_condition', to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('budget', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basics', to='user.userprofile')),
            ],
        ),
    ]
