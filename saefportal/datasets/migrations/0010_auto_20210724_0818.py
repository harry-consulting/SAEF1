# Generated by Django 3.1.6 on 2021-07-24 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0009_auto_20210720_0833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='azureconnection',
            old_name='db_name',
            new_name='database_name',
        ),
        migrations.RenameField(
            model_name='postgresconnection',
            old_name='db_name',
            new_name='database_name',
        ),
    ]
