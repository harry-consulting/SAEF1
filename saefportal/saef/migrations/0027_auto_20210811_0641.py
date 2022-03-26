# Generated by Django 3.1.6 on 2021-08-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saef', '0026_auto_20210810_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='email_host',
            field=models.CharField(default='localhost', max_length=50),
        ),
        migrations.AddField(
            model_name='settings',
            name='email_host_password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='settings',
            name='email_host_user',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='settings',
            name='email_port',
            field=models.IntegerField(default=587),
        ),
        migrations.AddField(
            model_name='settings',
            name='email_use_tls',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='try_live_connection',
            field=models.BooleanField(default=False),
        ),
    ]