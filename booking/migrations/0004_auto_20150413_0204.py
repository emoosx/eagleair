# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_flight_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='nationality',
        ),
    ]
