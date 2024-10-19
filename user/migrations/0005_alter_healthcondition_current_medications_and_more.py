# Generated by Django 5.0.7 on 2024-10-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcondition',
            name='current_medications',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='healthcondition',
            name='genetic_history',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='healthcondition',
            name='health_complaints',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
