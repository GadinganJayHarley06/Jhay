# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_detail_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='subject',
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ManyToManyField(related_name='Details', to='student.Subject'),
        ),
    ]
