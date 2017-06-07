# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('subject', models.TextField(default='')),
                ('content', models.TextField(default='')),
                ('date', models.DateTimeField(verbose_name='date send')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField(verbose_name='date send')),
                ('status', models.CharField(max_length=10)),
                ('email', models.ForeignKey(to='welcome.Email')),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('mail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('mail', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=20)),
                ('api_key', models.CharField(max_length=200)),
                ('is_active', models.BooleanField()),
                ('sended_count', models.IntegerField(default=0)),
                ('error_count', models.IntegerField(default=0)),
                ('retry', models.IntegerField(default=5)),
            ],
        ),
        migrations.AddField(
            model_name='email',
            name='receiver',
            field=models.ForeignKey(to='welcome.Receiver'),
        ),
        migrations.AddField(
            model_name='email',
            name='sender',
            field=models.ForeignKey(to='welcome.Sender'),
        ),
    ]
