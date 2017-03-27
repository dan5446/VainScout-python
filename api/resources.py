from tastypie.resources import ModelResource
import brewlog.models as bl
from django.contrib.auth.models import User
from tastypie import fields
from actstream.models import Action, Follow
from tastypie.contrib.contenttypes.fields import GenericForeignKeyField


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        allowed_methods = ['get']


class BrewResource(ModelResource):
    created_by = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = bl.Brew.objects.all()
        allowed_methods = ['get']

class IngredientResource(ModelResource):
    manufacturer = fields.CharField(attribute='manufacturer')
    name = fields.CharField(attribute='name')
    type = fields.CharField(attribute='type')
    class Meta:
        queryset = bl.Ingredient.objects.all()
        allowed_methods = ['get']


class GrainResource(ModelResource):
    class Meta:
        queryset = bl.Grain.objects.all()
        allowed_methods = ['get']


class HopResource(ModelResource):
    class Meta:
        queryset = bl.Hop.objects.all()
        allowed_methods = ['get']


class AdditiveResource(ModelResource):
    class Meta:
        queryset = bl.Additive.objects.all()
        allowed_methods = ['get']


class RecipeResource(ModelResource):
    class Meta:
        queryset = bl.Recipe.objects.all()
        allowed_methods = ['get']


class BoilResource(ModelResource):
    class Meta:
        queryset = bl.Boil.objects.all()
        allowed_methods = ['get']


class MashRestResource(ModelResource):
    class Meta:
        queryset = bl.MashRest.objects.all()
        allowed_methods = ['get']


class MashResource(ModelResource):
    class Meta:
        queryset = bl.Mash.objects.all()
        allowed_methods = ['get']


class MashStepResource(ModelResource):
    class Meta:
        queryset = bl.MashStep.objects.all()
        allowed_methods = ['get']


class FermentationStageResource(ModelResource):
    class Meta:
        queryset = bl.FermentationStage.objects.all()
        allowed_methods = ['get']


class FermentationResource(ModelResource):
    class Meta:
        queryset = bl.Fermentation.objects.all()
        allowed_methods = ['get']


class FermentationStepResource(ModelResource):
    class Meta:
        queryset = bl.FermentationStep.objects.all()
        allowed_methods = ['get']


class ActionResource(ModelResource):
    description = GenericForeignKeyField({
        User: UserResource,
        bl.Ingredient: IngredientResource,
        bl.Fermentation: FermentationResource
    }, 'actor')
    class Meta:
        queryset = Action.objects.all()
        allowed_methods = ['get']


class FollowResource(ModelResource):
    class Meta:
        queryset = Follow.objects.all()
        allowed_methods = ['get']




