# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20161006_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='book_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='book_id',
            field=models.IntegerField(default=datetime.datetime(2016, 10, 6, 11, 42, 51, 271703, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
