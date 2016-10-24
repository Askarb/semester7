# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='book_id',
            field=models.ForeignKey(to='book.Books'),
        ),
    ]
