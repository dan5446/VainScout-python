# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Additive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('function', models.CharField(max_length=1, choices=[(b'S', b'Sugars'), (b'F', b'Finings'), (b'R', b'Spices'), (b'N', b'Nutrients'), (b'O', b'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Boil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_duration', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('pre_volume', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('post_volume', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('volume_units', models.CharField(blank=True, max_length=1, null=True, choices=[(b'I', b'Gal'), (b'M', b'L')])),
                ('strength', models.CharField(default=b'M', max_length=1, choices=[(b'S', b'Soft'), (b'M', b'Medium'), (b'V', b'Vigorous')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brewer', models.CharField(max_length=80)),
                ('brew_date', models.DateField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('boil', models.ForeignKey(blank=True, to='brewlog.Boil', null=True)),
                ('created_by', models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fermentation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'A', max_length=1, choices=[(b'L', b'Lager'), (b'A', b'Ale'), (b'O', b'Other')])),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FermentationStage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('temp', models.PositiveSmallIntegerField()),
                ('units', models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Degrees F'), (b'C', b'Degrees C')])),
                ('type', models.CharField(max_length=80, null=True, blank=True)),
                ('vessel', models.CharField(max_length=80, null=True, blank=True)),
                ('additions', models.ManyToManyField(to='brewlog.Additive', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FermentationStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField(default=1)),
                ('fermentation', models.ForeignKey(to='brewlog.Fermentation', null=True)),
                ('step', models.ForeignKey(to='brewlog.FermentationStage', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('weight_units', models.CharField(default=b'I', max_length=1, choices=[(b'I', b'lbs'), (b'M', b'Kg'), (b'O', b'oz'), (b'G', b'grams')])),
                ('lovibond', models.DecimalField(max_digits=5, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alpha_percentage', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
                ('weight', models.DecimalField(null=True, max_digits=4, decimal_places=2, blank=True)),
                ('weight_units', models.CharField(default=b'I', max_length=1, choices=[(b'I', b'lbs'), (b'M', b'Kg'), (b'O', b'oz'), (b'G', b'grams')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manufacturer', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('type', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'I', max_length=1, choices=[(b'I', b'Single Infusion'), (b'T', b'Temperature'), (b'D', b'Decoction'), (b'S', b'Step')])),
                ('duration', models.DecimalField(default=b'60.00', max_digits=4, decimal_places=2)),
                ('water_volume', models.DecimalField(default=b'7.5', max_digits=6, decimal_places=2)),
                ('volume_units', models.CharField(default=b'I', max_length=1, choices=[(b'I', b'Gal'), (b'M', b'L')])),
                ('target_ph', models.DecimalField(default=b'5.4', max_digits=3, decimal_places=2)),
                ('begin_ph', models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True)),
                ('adjusted_ph', models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True)),
                ('final_ph', models.DecimalField(null=True, max_digits=3, decimal_places=2, blank=True)),
                ('adjustments', models.ManyToManyField(to='brewlog.Additive', null=True, blank=True)),
                ('grain_bill', models.ManyToManyField(to='brewlog.Grain')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MashRest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('temp', models.PositiveSmallIntegerField()),
                ('units', models.CharField(default=b'F', max_length=1, choices=[(b'F', b'Degrees F'), (b'C', b'Degrees C')])),
                ('type', models.CharField(max_length=80, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MashStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.PositiveIntegerField()),
                ('mash', models.ForeignKey(to='brewlog.Mash')),
                ('step', models.ForeignKey(to='brewlog.MashRest')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('style', models.CharField(max_length=40)),
                ('target_volume', models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)),
                ('volume_units', models.CharField(default=b'I', max_length=1, choices=[(b'I', b'Gal'), (b'M', b'L')])),
                ('target_gravity', models.DecimalField(null=True, max_digits=8, decimal_places=4, blank=True)),
                ('gravity_units', models.CharField(default=b'G', max_length=1, choices=[(b'P', b'Degrees Plato'), (b'G', b'Specific Gravity'), (b'B', b'Brix')])),
                ('additions', models.ManyToManyField(to='brewlog.Additive', null=True)),
                ('grain_bill', models.ManyToManyField(to='brewlog.Grain')),
                ('hop_bill', models.ManyToManyField(to='brewlog.Hop')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mash',
            name='steps',
            field=models.ManyToManyField(related_name='in_mash', through='brewlog.MashStep', to='brewlog.MashRest'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hop',
            name='type',
            field=models.ForeignKey(to='brewlog.Ingredient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='grain',
            name='type',
            field=models.ForeignKey(to='brewlog.Ingredient'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fermentationstage',
            name='dry_hops',
            field=models.ManyToManyField(to='brewlog.Hop', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fermentation',
            name='stages',
            field=models.ManyToManyField(related_name='in_ferm', through='brewlog.FermentationStep', to='brewlog.FermentationStage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='mash',
            field=models.ForeignKey(blank=True, to='brewlog.Mash', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='recipe',
            field=models.ForeignKey(to='brewlog.Recipe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brew',
            name='updated_by',
            field=models.ForeignKey(related_name='updater', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='additive',
            name='type',
            field=models.ForeignKey(to='brewlog.Ingredient'),
            preserve_default=True,
        ),
    ]
