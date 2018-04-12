# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-07 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=10, null=True)),
                ('forename', models.CharField(max_length=125, null=True)),
                ('lastname', models.CharField(max_length=125, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('emoji', models.CharField(max_length=255, null=True)),
                ('published_at', models.DateTimeField(null=True)),
                ('collaborators', models.ManyToManyField(related_name='documents', to='profiles.Profile')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created', to='profiles.Profile')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='projects.Document')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('size', models.FloatField()),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Oss',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('bucket', models.CharField(blank=True, max_length=255)),
                ('object', models.CharField(blank=True, max_length=255)),
                ('mine_type', models.CharField(blank=True, max_length=255)),
                ('size', models.FloatField()),
                ('etag', models.CharField(max_length=255, null=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000, null=True)),
                ('abstract', models.TextField(null=True)),
                ('year', models.PositiveIntegerField(null=True)),
                ('month', models.PositiveIntegerField(null=True)),
                ('volume', models.CharField(max_length=10, null=True)),
                ('pages', models.CharField(max_length=20, null=True)),
                ('page_from', models.CharField(max_length=10, null=True)),
                ('page_to', models.CharField(max_length=10, null=True)),
                ('authors', models.ManyToManyField(related_name='papers', to='projects.Author')),
                ('journal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='papers', to='projects.Journal')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('summary', models.TextField(null=True)),
                ('color', models.CharField(max_length=10, null=True)),
                ('publicStatus', models.BooleanField(default=True)),
                ('readme', models.TextField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libraries', to='profiles.Profile')),
                ('files', models.ManyToManyField(related_name='projects', to='projects.File')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='oss',
            name='paper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='projects.Paper'),
        ),
        migrations.AddField(
            model_name='file',
            name='oss',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='projects.Oss'),
        ),
        migrations.AddField(
            model_name='document',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='projects.Project'),
        ),
        migrations.AddField(
            model_name='document',
            name='stars',
            field=models.ManyToManyField(related_name='starred', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='document',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updated', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='document',
            name='views',
            field=models.ManyToManyField(related_name='viewed', to='profiles.Profile'),
        ),
    ]
