# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=16, verbose_name=b'Model')),
                ('seat_count_F', models.IntegerField(default=0, max_length=3)),
                ('seat_count_B', models.IntegerField(default=0, max_length=3)),
                ('seat_count_E', models.IntegerField(default=0, max_length=3)),
                ('seats_in_a_row_F', models.IntegerField(default=0)),
                ('seats_in_a_row_B', models.IntegerField(default=0)),
                ('seats_in_a_row_E', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='flight',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='flight',
            name='seats',
        ),
        migrations.AddField(
            model_name='flight',
            name='aircraft',
            field=models.ForeignKey(blank=True, to='flight.Aircraft', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='price_B',
            field=models.FloatField(default=b'4500', verbose_name=b'Price Business Class'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='price_E',
            field=models.FloatField(default=b'400', verbose_name=b'Price Economy Class'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='flight',
            name='price_F',
            field=models.FloatField(default=b'25000', verbose_name=b'Price First Class'),
            preserve_default=True,
        ),
    ]
