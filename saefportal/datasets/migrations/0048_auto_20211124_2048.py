# Generated by Django 3.1.6 on 2021-11-24 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0047_auto_20211123_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='type',
            field=models.CharField(choices=[('POSTGRES', 'PostgreSQL'), ('AZURE', 'Azure SQL'), ('ONEDRIVE', 'OneDrive'), ('GOOGLE_DRIVE', 'Google Drive'), ('DROPBOX', 'Dropbox'), ('GOOGLE_CLOUD_STORAGE', 'Google Cloud Storage'), ('AZURE_BLOB_STORAGE', 'Azure Blob Storage'), ('AZURE_DATA_LAKE', 'Azure Data Lake')], max_length=128),
        ),
    ]
