# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-21 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddslingers', '0008_user_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='expire_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]