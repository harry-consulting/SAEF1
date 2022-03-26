# Generated by Django 3.1.6 on 2021-12-15 08:21

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datastores', '0013_auto_20211215_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='azureblobstoragedatastore',
            name='connection_string',
            field=fernet_fields.fields.EncryptedCharField(max_length=256),
        ),
    ]