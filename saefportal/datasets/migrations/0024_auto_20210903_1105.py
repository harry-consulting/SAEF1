# Generated by Django 3.1.6 on 2021-09-03 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0023_auto_20210903_1100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='extraction_table',
            new_name='table',
        ),
        migrations.RenameField(
            model_name='historicaldataset',
            old_name='extraction_table',
            new_name='table',
        ),
    ]
