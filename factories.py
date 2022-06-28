from factory import django, fuzzy

from pokemon.models import Pokemon


class PokemonFactory(django.DjangoModelFactory):
    name = fuzzy.FuzzyText()
    description = fuzzy.FuzzyText()
    ability = fuzzy.FuzzyText()
    species = fuzzy.FuzzyText()
    defense = fuzzy.FuzzyInteger(1, 100, step=1)

    class Meta:
        model = Pokemon
