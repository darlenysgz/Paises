# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('poblacion', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='lenguaje',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('lenguaje_nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='pais',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('codigo', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=25)),
                ('continente', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='lenguaje_pais',
            field=models.ForeignKey(to='myapp_list.pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='ciudad_pais',
            field=models.ForeignKey(to='myapp_list.pais'),
        ),
    ]
