# Generated by Django 3.1.6 on 2021-09-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20210924_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectpermission',
            name='permission_level',
        ),
        migrations.AddField(
            model_name='objectpermission',
            name='can_delete',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='objectpermission',
            name='can_execute',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='objectpermission',
            name='can_update',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='objectpermission',
            name='can_view',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]