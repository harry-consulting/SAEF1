# Generated by Django 3.1.6 on 2021-10-25 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0038_auto_20211021_1201'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AzureBlobStorageConnection',
        ),
    ]
