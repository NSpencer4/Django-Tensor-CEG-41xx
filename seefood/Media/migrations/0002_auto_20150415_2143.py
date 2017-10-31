# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Media', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='album',
            new_name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='comments',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
