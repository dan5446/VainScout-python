# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('brewlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brew',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='brew',
            name='updated_on',
        ),
        migrations.AddField(
            model_name='brew',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False),
            preserve_default=True,
        ),
    ]
