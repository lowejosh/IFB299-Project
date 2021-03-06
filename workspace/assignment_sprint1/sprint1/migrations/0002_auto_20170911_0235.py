# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprint1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='accountType',
            field=models.CharField(max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(max_length=63, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastName',
            field=models.CharField(max_length=63, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dateOfBirth',
            field=models.DateField(null=True),
        ),
    ]
