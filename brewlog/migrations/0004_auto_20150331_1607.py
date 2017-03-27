# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brewlog', '0003_auto_20150331_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basemodel',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='basemodel',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='BaseModel',
        ),
    ]
