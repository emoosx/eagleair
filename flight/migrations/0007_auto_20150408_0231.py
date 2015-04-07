# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_auto_20150405_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='seat_count_B',
            field=models.IntegerField(default=20, max_length=3, verbose_name=b'Business Class Seats'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='seat_count_E',
            field=models.IntegerField(default=60, max_length=3, verbose_name=b'Economy Class Seats'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='seat_count_F',
            field=models.IntegerField(default=6, max_length=3, verbose_name=b'First Class Seats'),
            preserve_default=True,
        ),
    ]
