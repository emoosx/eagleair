# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_auto_20150401_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraft',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 17, 20, 59, 947088), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airline',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 17, 21, 12, 447530), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='airport',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 17, 21, 17, 774317), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_date',
            field=models.DateField(default=b'1990-01-01', verbose_name=b'Arrival Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=b'08:00', verbose_name=b'Arrival Time'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 17, 21, 22, 885122), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_date',
            field=models.DateField(default=b'1990-01-01', verbose_name=b'Depature Date'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=b'08:00', verbose_name=b'Depature Time'),
            preserve_default=True,
        ),
    ]
