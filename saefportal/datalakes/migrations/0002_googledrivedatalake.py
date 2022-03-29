# Generated by Django 3.1.6 on 2021-11-09 07:22

from django.db import migrations, models
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datalakes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleDriveDatalake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('root_path', models.CharField(blank=True, default='', max_length=500)),
                ('token_cache', fernet_fields.fields.EncryptedTextField()),
            ],
        ),
    ]
