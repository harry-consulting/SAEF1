# Generated by Django 3.1.6 on 2021-09-03 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0022_auto_20210903_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='extraction_sql',
            new_name='query',
        ),
        migrations.RenameField(
            model_name='historicaldataset',
            old_name='extraction_sql',
            new_name='query',
        ),
    ]