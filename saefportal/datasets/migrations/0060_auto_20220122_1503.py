# Generated by Django 3.1.6 on 2022-01-22 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0059_remove_connection_time_out'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='dataset',
            name='Name uniqueness',
        ),
    ]
