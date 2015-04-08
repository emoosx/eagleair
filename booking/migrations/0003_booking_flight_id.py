# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0007_auto_20150408_0231'),
        ('booking', '0002_auto_20150401_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='flight_id',
            field=models.ForeignKey(default=1, verbose_name=b'Flight', to='flight.Flight'),
            preserve_default=False,
        ),
    ]
