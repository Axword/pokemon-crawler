from django.test import TestCase
from django.urls import reverse
from factories import PokemonFactory


class TestPokemonViews(TestCase):

    def test_retrive_list(self):
        PokemonFactory()
        response = self.client.get(reverse('pokemon-list'))
        assert response.status_code == 200
        assert len(response.json()) == 1

    def test_get_pokemon(self):
        pokemon = PokemonFactory()
        response = self.client.get(
            reverse('pokemon-detail', kwargs={'pokemon_name': pokemon.name}))
        assert response.status_code == 200
        assert pokemon.name == response.json()[0]['fields']['name']

    def test_get_invalid_pokemon(self):
        pokemon = PokemonFactory(name='abc')
        response = self.client.get(
            reverse('pokemon-detail', kwargs={'pokemon_name': 'ab'}))
        assert response.status_code == 404
        assert 'Pokemon with name: ab' in str(response.content)
