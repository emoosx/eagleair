# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0005_auto_20150404_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='airport',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'City'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='airport',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'Name'),
            preserve_default=True,
        ),
    ]
