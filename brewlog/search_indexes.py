
from haystack import indexes
from .models import Ingredient


class IngredientIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    manufacturer = indexes.CharField(model_attr='manufacturer')
    name = indexes.CharField(model_attr='name')
    type = indexes.NgramField(model_attr='type')

    def get_model(self):
        return Ingredient

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()