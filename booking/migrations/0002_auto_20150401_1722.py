# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='creation_date',
        ),
        migrations.AddField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 1, 17, 22, 52, 45989), verbose_name=b'Created At', auto_now_add=True),
            preserve_default=False,
        ),
    ]
