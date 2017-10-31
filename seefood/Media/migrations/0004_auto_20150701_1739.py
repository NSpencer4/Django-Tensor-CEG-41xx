# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0003_auto_20150610_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='added_on',
            field=models.DateField(default=datetime.datetime(2015, 7, 1, 17, 39, 19, 828396, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='Media.Post'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='thumb',
            field=models.ImageField(upload_to=b'thumbnails', editable=False),
        ),
    ]
