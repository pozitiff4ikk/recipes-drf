# Generated by Django 3.2.9 on 2021-11-15 12:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0003_reciper'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reciper',
            new_name='Recipe',
        ),
    ]
