
from tastypie.api import Api
import api.resources as rcs

v1_api = Api(api_name='v1')
v1_api.register(rcs.UserResource())
v1_api.register(rcs.AdditiveResource())
v1_api.register(rcs.BoilResource())
v1_api.register(rcs.FermentationResource())
v1_api.register(rcs.GrainResource())
v1_api.register(rcs.BrewResource())
v1_api.register(rcs.HopResource())
v1_api.register(rcs.IngredientResource())
v1_api.register(rcs.MashResource())
v1_api.register(rcs.RecipeResource())
v1_api.register(rcs.ActionResource())
v1_api.register(rcs.FollowResource())