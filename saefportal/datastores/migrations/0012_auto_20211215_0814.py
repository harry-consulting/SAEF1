# Generated by Django 3.1.6 on 2021-12-15 08:14

from django.db import migrations
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datastores', '0011_amazons3datastore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amazons3datastore',
            name='access_key_id',
            field=fernet_fields.fields.EncryptedCharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='amazons3datastore',
            name='secret_access_key',
            field=fernet_fields.fields.EncryptedCharField(max_length=128),
        ),
    ]