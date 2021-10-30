# Generated by Django 3.2.4 on 2021-10-30 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('label', models.CharField(blank=True, max_length=200, null=True)),
                ('isEncrypted', models.BooleanField(default=False)),
                ('properties', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionParamValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ConnectionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomSchedule',
            fields=[
                ('crontabschedule_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_celery_beat.crontabschedule')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            bases=('django_celery_beat.crontabschedule',),
        ),
        migrations.CreateModel(
            name='NotebookJob',
            fields=[
                ('periodictask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_celery_beat.periodictask')),
                ('notebookId', models.CharField(db_index=True, max_length=50, unique=True)),
            ],
            bases=('django_celery_beat.periodictask',),
        ),
        migrations.CreateModel(
            name='NotebookObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notebookZeppelinId', models.CharField(max_length=10)),
                ('defaultPayload', models.JSONField(default={})),
            ],
        ),
        migrations.CreateModel(
            name='NotebookRunLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTimestamp', models.DateTimeField(auto_now_add=True)),
                ('endTimestamp', models.DateTimeField(default=None, null=True)),
                ('updateTimestamp', models.DateTimeField(auto_now=True)),
                ('notebookId', models.CharField(default='000000000', max_length=20)),
                ('logs', models.TextField(default='{}')),
                ('status', models.CharField(max_length=20)),
                ('runType', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.CharField(default=None, max_length=5000, null=True)),
                ('taskId', models.CharField(default='', max_length=200)),
                ('zeppelinServerId', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NotebookTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.JSONField(default={})),
                ('formJson', models.JSONField(default={})),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
