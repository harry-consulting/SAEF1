# Generated by Django 3.1.6 on 2021-08-02 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saef', '0020_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationsession',
            name='application',
        ),
        migrations.RemoveField(
            model_name='applicationsessionmetadata',
            name='application_session',
        ),
        migrations.RemoveField(
            model_name='azureblobstorageconnection',
            name='connection',
        ),
        migrations.RemoveField(
            model_name='azureconnection',
            name='connection',
        ),
        migrations.RemoveField(
            model_name='columnprofilehistory',
            name='column',
        ),
        migrations.RemoveField(
            model_name='columnprofilehistory',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='columnprofilehistory',
            name='job_session',
        ),
        migrations.RemoveField(
            model_name='connection',
            name='connection_type',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='connection',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='job',
        ),
        migrations.RemoveField(
            model_name='datasetmetadatacolumn',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='datasetmetadataconstraint',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='datasetprofilehistory',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='datasetprofilehistory',
            name='job_session',
        ),
        migrations.RemoveField(
            model_name='datasetprofileoperationhistory',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='datasetsession',
            name='dataset',
        ),
        migrations.RemoveField(
            model_name='datasetsession',
            name='job_session',
        ),
        migrations.RemoveField(
            model_name='datasetsessionmetadata',
            name='dataset_session',
        ),
        migrations.RemoveField(
            model_name='datasource',
            name='source',
        ),
        migrations.RemoveField(
            model_name='job',
            name='application',
        ),
        migrations.RemoveField(
            model_name='jobsession',
            name='application_session',
        ),
        migrations.RemoveField(
            model_name='jobsession',
            name='job',
        ),
        migrations.RemoveField(
            model_name='jobsessionmetadata',
            name='job_session',
        ),
        migrations.RemoveField(
            model_name='jobsessionstatus',
            name='job_session',
        ),
        migrations.RemoveField(
            model_name='postgresconnection',
            name='connection',
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='ApplicationSession',
        ),
        migrations.DeleteModel(
            name='ApplicationSessionMetaData',
        ),
        migrations.DeleteModel(
            name='ApplicationToken',
        ),
        migrations.DeleteModel(
            name='AzureBlobStorageConnection',
        ),
        migrations.DeleteModel(
            name='AzureConnection',
        ),
        migrations.DeleteModel(
            name='ColumnProfileHistory',
        ),
        migrations.DeleteModel(
            name='Connection',
        ),
        migrations.DeleteModel(
            name='ConnectionType',
        ),
        migrations.DeleteModel(
            name='Dataset',
        ),
        migrations.DeleteModel(
            name='DatasetMetadataColumn',
        ),
        migrations.DeleteModel(
            name='DatasetMetadataConstraint',
        ),
        migrations.DeleteModel(
            name='DatasetProfileHistory',
        ),
        migrations.DeleteModel(
            name='DatasetProfileOperationHistory',
        ),
        migrations.DeleteModel(
            name='DatasetSession',
        ),
        migrations.DeleteModel(
            name='DatasetSessionMetaData',
        ),
        migrations.DeleteModel(
            name='Datasource',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='JobSession',
        ),
        migrations.DeleteModel(
            name='JobSessionMetaData',
        ),
        migrations.DeleteModel(
            name='JobSessionStatus',
        ),
        migrations.DeleteModel(
            name='PostgresConnection',
        ),
    ]