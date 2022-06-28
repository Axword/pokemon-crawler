import logging

import requests
from django.db import transaction
from django.forms.models import model_to_dict
from pokemon.models import Pokemon

from app.misc import serialize_pokemon


@transaction.atomic
def add_new_pokemons():
    qs_len = len(Pokemon.objects.all())
    try:
        response = requests.get(
            'https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0')
    except Exception:
        return "Server unreachable"
    pokemons_data = response.json()['results']
    if qs_len < len(pokemons_data):
        list_of_new_pokemons = []
        for pokemon in pokemons_data[qs_len:]:
            name = pokemon['name']
            poke_details = requests.get(
                f'https://pokeapi.co/api/v2/pokemon/{name}').json()
            new_pokemon = Pokemon(**serialize_pokemon(poke_details))
            list_of_new_pokemons.append(new_pokemon)
            Pokemon.objects.bulk_create(list_of_new_pokemons)
    else:
        logging.info("No new pokemons discovered")


@transaction.atomic
def check_data_on_old_pokemons():
    qs = Pokemon.objects.all()
    for pokemon in qs:
        poke_dict = model_to_dict(pokemon)
        del poke_dict['id']
        poke_details = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{poke_dict["name"]}').json()
        db_pokemon = serialize_pokemon(poke_details)
        if db_pokemon != poke_dict:
            pokemon.update(*poke_dict)
            pokemon.save()
