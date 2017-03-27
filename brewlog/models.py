from django.db import models
from django.contrib.auth.models import User #TODO: Consider providing an app user model which ties to User and adds app related info
from model_utils.models import TimeStampedModel
from model_utils import Choices
from django.utils.translation import ugettext_lazy as _
import reversion


WEIGHT_UNITS = Choices('lbs','Kg','oz','grams')
VOLUME_UNITS = Choices('Gal','L')
GRAVITY_UNITS = Choices(('DP', _('Degrees Plato')),('SG', _('Specific Gravity')),('BX', _('Brix')))

class Ingredient(models.Model):
    manufacturer = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)

    class Meta:
        unique_together = (("manufacturer", "name", "type"),)

    def __unicode__(self):
        return '{0} {1} {2}'.format(self.manufacturer, self.name, self.type)

class Grain(models.Model): #http://www.northernbrewer.com/shop/briess-2-row-brewers-malt-1.html for more details
    type = models.ForeignKey(Ingredient)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    weight_units = models.CharField(max_length=5, choices=WEIGHT_UNITS, default=WEIGHT_UNITS.lbs)
    lovibond = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    def __unicode__(self):
        return '{0}{1} {2}'.format(self.weight, self.get_weight_units_display(), self.type.name)


class Hop(models.Model):
    type = models.ForeignKey(Ingredient)
    alpha_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    weight_units = models.CharField(max_length=5, choices=WEIGHT_UNITS, default=WEIGHT_UNITS.oz)

    def __unicode__(self):
        return '{0}{1} {2}'.format(self.alpha_percentage, 'a', str(self.type))


class Additive(models.Model):
    ADDITIVE_TYPES = (
        ('S', 'Sugars'),
        ('F', 'Finings'),
        ('R', 'Spices'),
        ('N', 'Nutrients'),
        ('O', 'Other'),
    )
    type = models.ForeignKey(Ingredient)
    function = models.CharField(max_length=1, choices=ADDITIVE_TYPES)

    def __unicode__(self):
        return '{0}: {1} {2} {3}'.format(self.get_function_display(), self.type.manufacturer, self.type.name, self.type.type)


class Recipe(models.Model):
    name = models.CharField(max_length=40)
    style = models.CharField(max_length=40) #TODO: Might want to make this a foreign key to styles
    target_volume = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    volume_units = models.CharField(max_length=5, choices=VOLUME_UNITS, default=VOLUME_UNITS.Gal)
    target_gravity = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    gravity_units = models.CharField(max_length=2, choices=GRAVITY_UNITS, default=GRAVITY_UNITS.SG)
    grain_bill = models.ManyToManyField(Grain)
    hop_bill = models.ManyToManyField(Hop)
    additions = models.ManyToManyField(Additive, null=True)
    # notes

    def __unicode__(self):
        return '{0} {1}'.format(self.name, self.style)


class Boil(models.Model):
    STRENGTH_CHOICES = (
        ('S', 'Soft'),
        ('M', 'Medium'),
        ('V', 'Vigorous'),
    )
    total_duration = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    pre_volume = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    post_volume = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    volume_units = models.CharField(max_length=5, choices=VOLUME_UNITS, blank=True, null=True)
    strength = models.CharField(max_length=1, choices=STRENGTH_CHOICES, default='M')

    def __unicode__(self):
        return '{0} {1} {2}{3}'.format(self.total_duration, 'minute boil', self.post_volume, self.get_volume_units_display())


class MashRest(models.Model):
    TEMP_CHOICES = (
        ('F', 'Degrees F'),
        ('C', 'Degrees C'),
    )
    time = models.PositiveSmallIntegerField(blank=True, null=True)
    temp = models.PositiveSmallIntegerField()
    units = models.CharField(max_length=1, choices=TEMP_CHOICES, default='F')
    type = models.CharField(max_length=80, blank=True, null=True)

    def __unicode__(self):
        return '{0} {1} {2} {3}{4}'.format(self.time, 'minute', self.type, self.temp, self.units)


class Mash(models.Model):
    MASH_CHOICES = (
        ('I', 'Single Infusion'),
        ('T', 'Temperature'),
        ('D', 'Decoction'),
        ('S', 'Step'),
    )
    type = models.CharField(max_length=1, choices=MASH_CHOICES, default='I')
    duration = models.DecimalField(max_digits=4, decimal_places=2, default='60.00')
    steps = models.ManyToManyField(MashRest, related_name='in_mash', through='MashStep')
    grain_bill= models.ManyToManyField(Grain)
    water_volume = models.DecimalField(max_digits=6, decimal_places=2, default='7.5')
    volume_units = models.CharField(max_length=1, choices=VOLUME_UNITS, default=VOLUME_UNITS.Gal)
    target_ph = models.DecimalField(max_digits=3, decimal_places=2, default='5.4')
    begin_ph = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    adjusted_ph = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    final_ph = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    adjustments = models.ManyToManyField(Additive, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Mashes"

    def __unicode__(self):
        return '{0} {1} {2} {3}'.format(self.duration, 'minute', self.get_type_display(), 'mash')


class MashStep(models.Model):
    # Through table for ordering mash steps
    number = models.PositiveIntegerField()
    mash = models.ForeignKey(Mash)
    step = models.ForeignKey(MashRest)

class FermentationStage(models.Model):
    TEMP_CHOICES = (
        ('F', 'Degrees F'),
        ('C', 'Degrees C'),
    )
    time = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    temp = models.PositiveSmallIntegerField()
    units = models.CharField(max_length=1, choices=TEMP_CHOICES, default='F')
    type = models.CharField(max_length=80, blank=True, null=True)
    vessel = models.CharField(max_length=80, blank=True, null=True)
    additions = models.ManyToManyField(Additive, blank=True, null=True)
    dry_hops = models.ManyToManyField(Hop, blank=True, null=True)

    def __unicode__(self):
        return '{0} {1} {2} {3}{4}'.format(self.time, 'Day', self.type, self.temp, self.units)


class Fermentation(models.Model):
    FERMENTATION_TYPES = (
        ('L', 'Lager'),
        ('A', 'Ale'),
        ('O', 'Other'),
    )
    type = models.CharField(max_length=1, choices=FERMENTATION_TYPES, default='A')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    stages = models.ManyToManyField(FermentationStage, related_name='in_ferm', through='FermentationStep')

    def __unicode__(self):
        return '{0} {1} {2} {3} {4} {5}'.format(self.get_type_display(), 'Fermentation,' , 'from', self.start_date, 'until', self.end_date)

class FermentationStep(models.Model):
    # Through table for ordering fermentation steps
    number = models.PositiveIntegerField(default=1)
    fermentation = models.ForeignKey(Fermentation, null=True)
    step = models.ForeignKey(FermentationStage, null=True)


class Brew(TimeStampedModel):
    brewer = models.CharField(max_length=80)
    brew_date = models.DateField(blank=True, null=False)
    created_by = models.ForeignKey(User, related_name='creator')
    updated_by = models.ForeignKey(User, related_name='updater')
    recipe = models.ForeignKey(Recipe)
    #   sanitize
    mash = models.ForeignKey(Mash, blank=True, null=True)
    boil = models.ForeignKey(Boil, blank=True, null=True)
    #ferment = models.ForeignKey(Fermentation, blank=True, null=True)
    #   package
    #   checklist

    def __unicode__(self):
        return '{0}.{1}.{2}.{3}'.format(self.brewer.name, self.recipe.style, self.recipe.name, self.brew_date)





