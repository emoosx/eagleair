# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('iata_code', models.CharField(max_length=3, null=True, verbose_name=b'IATA Code', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Airlines',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('iata_code', models.CharField(max_length=3, serialize=False, verbose_name=b'IATA Code', primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('city', models.CharField(max_length=100, verbose_name=b'City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=7, verbose_name=b'Flight Code')),
                ('seats', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('airline', models.ForeignKey(to='flight.Airline')),
                ('from_airport', models.ForeignKey(related_name='from_airport', to='flight.Airport')),
                ('to_airport', models.ForeignKey(related_name='to_airport', to='flight.Airport')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='airport',
            name='country',
            field=models.ForeignKey(to='flight.Country'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='airline',
            name='country',
            field=models.ForeignKey(to='flight.Country'),
            preserve_default=True,
        ),
    ]
