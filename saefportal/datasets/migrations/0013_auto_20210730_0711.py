# Generated by Django 3.1.6 on 2021-07-30 07:11

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0012_auto_20210729_0532'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasetrun',
            old_name='create_timestamp',
            new_name='start_time',
        ),
        migrations.AddField(
            model_name='datasetrun',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='connection',
            name='key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
