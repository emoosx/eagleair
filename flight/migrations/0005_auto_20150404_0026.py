# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_auto_20150401_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='seat_count_B',
            field=models.IntegerField(default=20, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='seat_count_E',
            field=models.IntegerField(default=60, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='seat_count_F',
            field=models.IntegerField(default=6, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='seats_in_a_row_B',
            field=models.IntegerField(default=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='seats_in_a_row_E',
            field=models.IntegerField(default=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='seats_in_a_row_F',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
    ]
