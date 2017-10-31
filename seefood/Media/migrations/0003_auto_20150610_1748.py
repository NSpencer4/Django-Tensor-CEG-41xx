# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0002_auto_20150415_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumb',
            field=models.ImageField(default=datetime.datetime(2015, 6, 10, 17, 48, 49, 316147, tzinfo=utc), upload_to=b'thumbnails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to=b'photos'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(related_name='photos', to='Media.Post'),
        ),
    ]
