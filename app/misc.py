def create_description(poke_details):
    return f'{poke_details["name"]} - is a Pokemon from a {poke_details["species"]["name"]} species.'


def serialize_pokemon(poke_details):
    abilites = poke_details['abilities'][0]['ability']['name'] if poke_details['abilities'] else None
    return {
        'name': poke_details['name'],
        'description': create_description(poke_details),
        'ability': abilites,
        'species': poke_details['species']['name'],
        'defense': poke_details['stats'][3]['base_stat']
    }
