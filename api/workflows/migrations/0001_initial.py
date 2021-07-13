# Generated by Django 3.2.4 on 2021-07-11 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0015_edit_solarschedule_events_choices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('triggerWorkflowStatus', models.CharField(default='SUCCESS', max_length=50)),
                ('periodictask', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.periodictask')),
                ('triggerWorkflow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflows.workflow')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='SUCCESS', max_length=50)),
                ('startTimestamp', models.DateTimeField(auto_now_add=True)),
                ('endTimestamp', models.DateTimeField(default=None, null=True)),
                ('taskId', models.CharField(default='', max_length=200)),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow')),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowNotebookMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notebookId', models.CharField(default='000000000', max_length=20)),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.workflow')),
            ],
        ),
    ]
