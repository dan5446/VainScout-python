from django.forms import ModelForm
from .models import Ingredient


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['manufacturer','name','type']