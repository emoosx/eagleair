# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20150413_0204'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='taken_seats',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
