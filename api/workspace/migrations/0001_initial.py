# Generated by Django 3.2.4 on 2021-07-24 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='WorkspaceConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage', models.CharField(blank=True, max_length=100, null=True)),
                ('s3AccessKey', models.TextField(blank=True, null=True)),
                ('s3SecretKey', models.TextField(blank=True, null=True)),
                ('googleKey', models.TextField(blank=True, null=True)),
                ('azureAccount', models.TextField(blank=True, null=True)),
                ('azureKey', models.TextField(blank=True, null=True)),
                ('inactivityTimeout', models.IntegerField(default=600)),
                ('zeppelinServerImage', models.CharField(blank=True, max_length=200, null=True)),
                ('zeppelinInterpreterImage', models.CharField(blank=True, max_length=200, null=True)),
                ('sparkImage', models.CharField(blank=True, max_length=200, null=True)),
                ('acidProvider', models.CharField(blank=True, max_length=100, null=True)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.workspace')),
            ],
        ),
        migrations.CreateModel(
            name='KubernetesTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zeppelinServerTemplate', models.TextField(blank=True, null=True)),
                ('zeppelinJobServerTemplate', models.TextField(blank=True, null=True)),
                ('interpreterTemplate', models.TextField(blank=True, null=True)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.workspace')),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workspace.workspace')),
            ],
        ),
    ]