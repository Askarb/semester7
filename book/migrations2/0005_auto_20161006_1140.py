# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20161006_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='book_id',
        ),
        migrations.AddField(
            model_name='customer',
            name='book_id',
            field=models.ManyToManyField(to='book.Books'),
        ),
    ]
