# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-18 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to=b'')),
            ],
        ),
    ]
