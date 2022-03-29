# Generated by Django 3.1.6 on 2021-09-03 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_auto_20210903_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaljob',
            name='template_task',
            field=models.CharField(blank=True, choices=[('PROFILE_DATASET', 'Profile dataset'), ('REFRESH_DATA', 'Refresh data'), ('EXTRACT_METADATA', 'Extract metadata')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='template_task',
            field=models.CharField(blank=True, choices=[('PROFILE_DATASET', 'Profile dataset'), ('REFRESH_DATA', 'Refresh data'), ('EXTRACT_METADATA', 'Extract metadata')], max_length=64, null=True),
        ),
        migrations.DeleteModel(
            name='TemplateTask',
        ),
    ]
