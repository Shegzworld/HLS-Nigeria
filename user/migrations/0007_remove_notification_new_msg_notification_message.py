# Generated by Django 5.0.7 on 2024-11-29 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_message_notification_new_msg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='new_msg',
        ),
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='user.message'),
        ),
    ]
