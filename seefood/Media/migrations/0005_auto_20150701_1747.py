# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0004_auto_20150701_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
