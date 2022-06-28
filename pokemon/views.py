from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

from pokemon.models import Pokemon


@require_http_methods(["GET"])
def get_pokemons_list(request, *args, **kwargs):
    qs = Pokemon.objects.all()
    data = serializers.serialize('json', qs)
    return HttpResponse(data, content_type='application/json')


@require_http_methods(["GET"])
def get_pokemon_details_by_name(request, pokemon_name, *args, **kwargs):
    try:
        instance = Pokemon.objects.get(name=pokemon_name)
        data = serializers.serialize('json', (instance,))
    except Exception:
        return HttpResponseNotFound((f'Pokemon with name: {pokemon_name} not found'))
    return HttpResponse(data, content_type='application/json')
