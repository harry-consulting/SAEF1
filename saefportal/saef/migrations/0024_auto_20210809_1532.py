# Generated by Django 3.1.6 on 2021-08-09 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saef', '0023_auto_20210809_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='dataset_update_frequency',
            new_name='dataset_refresh_frequency',
        ),
    ]
