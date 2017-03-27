from django.apps import AppConfig
from actstream import registry
from django.contrib.auth.models import User


class Dan5446Config(AppConfig):
    name = 'brewlog'
    verbose_name = 'Brew Log'

    def ready(self):
        registry.register(User)
        registry.register(self.get_model('Hop'), self.get_model('Ingredient'), self.get_model('Grain'), self.get_model('Mash'))
        registry.register(self.get_model('Fermentation'), self.get_model('FermentationStep'), self.get_model('Brew'))

