# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('brewlog', '0002_auto_20150327_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('created_by', models.ForeignKey(related_name='created_by_user', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(related_name='updated_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='mash',
            options={'verbose_name_plural': 'Mashes'},
        ),
        migrations.AlterField(
            model_name='boil',
            name='volume_units',
            field=models.CharField(blank=True, max_length=5, null=True, choices=[(b'Gal', b'Gal'), (b'L', b'L')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grain',
            name='weight_units',
            field=models.CharField(default=b'lbs', max_length=5, choices=[(b'lbs', b'lbs'), (b'Kg', b'Kg'), (b'oz', b'oz'), (b'grams', b'grams')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hop',
            name='weight_units',
            field=models.CharField(default=b'oz', max_length=5, choices=[(b'lbs', b'lbs'), (b'Kg', b'Kg'), (b'oz', b'oz'), (b'grams', b'grams')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mash',
            name='volume_units',
            field=models.CharField(default=b'Gal', max_length=1, choices=[(b'Gal', b'Gal'), (b'L', b'L')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='gravity_units',
            field=models.CharField(default=b'SG', max_length=2, choices=[(b'DP', 'Degrees Plato'), (b'SG', 'Specific Gravity'), (b'BX', 'Brix')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='volume_units',
            field=models.CharField(default=b'Gal', max_length=5, choices=[(b'Gal', b'Gal'), (b'L', b'L')]),
            preserve_default=True,
        ),
    ]
