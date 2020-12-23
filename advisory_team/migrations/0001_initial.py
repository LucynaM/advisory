# Generated by Django 3.1.3 on 2020-12-23 20:00

import advisory_team.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=255, verbose_name='specialization')),
            ],
            options={
                'verbose_name': 'Specialization',
                'verbose_name_plural': 'Specializations',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('photo_desktop', models.ImageField(blank=True, null=True, upload_to='images/desktop', verbose_name='photo desktop')),
                ('photo_mobile', models.ImageField(blank=True, null=True, upload_to='images/mobile', verbose_name='photo mobile')),
                ('first_name', models.CharField(max_length=64, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=64, verbose_name='last_name')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('academic_title', models.CharField(blank=True, max_length=32, null=True, verbose_name='academic_title')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=32, unique=True, validators=[advisory_team.models.only_int], verbose_name='phone')),
                ('html_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='html_id')),
                ('specializations', models.ManyToManyField(blank=True, null=True, related_name='team_members', to='advisory_team.Specialization', verbose_name='specializations')),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]
