import json

DATA_KEYS = [
    "abilities",
    "base_experience",
    "forms",
    "height",
    "id",
    "location_area_encounters",
    "moves",
    "name",
    "order",
    "species",
    "sprites",
    "stats",
    "types",
    "weight",
]

POKEMON_LIST = [
    {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
    {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
    {"name": "venusaur", "url": "https://pokeapi.co/api/v2/pokemon/3/"},
    {"name": "charmander", "url": "https://pokeapi.co/api/v2/pokemon/4/"},
    {"name": "charmeleon", "url": "https://pokeapi.co/api/v2/pokemon/5/"},
    {"name": "charizard", "url": "https://pokeapi.co/api/v2/pokemon/6/"},
    {"name": "squirtle", "url": "https://pokeapi.co/api/v2/pokemon/7/"},
    {"name": "wartortle", "url": "https://pokeapi.co/api/v2/pokemon/8/"},
    {"name": "blastoise", "url": "https://pokeapi.co/api/v2/pokemon/9/"},
    {"name": "caterpie", "url": "https://pokeapi.co/api/v2/pokemon/10/"},
    {"name": "metapod", "url": "https://pokeapi.co/api/v2/pokemon/11/"},
    {"name": "butterfree", "url": "https://pokeapi.co/api/v2/pokemon/12/"},
    {"name": "weedle", "url": "https://pokeapi.co/api/v2/pokemon/13/"},
    {"name": "kakuna", "url": "https://pokeapi.co/api/v2/pokemon/14/"},
    {"name": "beedrill", "url": "https://pokeapi.co/api/v2/pokemon/15/"},
    {"name": "pidgey", "url": "https://pokeapi.co/api/v2/pokemon/16/"},
    {"name": "pidgeotto", "url": "https://pokeapi.co/api/v2/pokemon/17/"},
    {"name": "pidgeot", "url": "https://pokeapi.co/api/v2/pokemon/18/"},
    {"name": "rattata", "url": "https://pokeapi.co/api/v2/pokemon/19/"},
    {"name": "raticate", "url": "https://pokeapi.co/api/v2/pokemon/20/"},
]

with open("tests/api/fixtures/pokemon-list.json", "r") as f:
    POKEMON_LIST_RESPONSE = json.load(f)

POKEMON_LIST_CACHED = '[{"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"}, {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}, {"name": "venusaur", "url": "https://pokeapi.co/api/v2/pokemon/3/"}, {"name": "charmander", "url": "https://pokeapi.co/api/v2/pokemon/4/"}, {"name": "charmeleon", "url": "https://pokeapi.co/api/v2/pokemon/5/"}]'

with open("tests/api/fixtures/pokemon-data.json", "r") as f:
    POKEMON_DATA_RESPONSE = json.load(f)

POKEMON_DATA_CACHED = '{"abilities": ["limber", "imposter"], "base_experience": 101, "forms": ["ditto"], "height": 3, "id": 132, "location_area_encounters": "https://pokeapi.co/api/v2/pokemon/132/encounters", "moves": ["transform"], "name": "ditto", "order": 203, "species": "ditto", "sprites": ["https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/shiny/132.png", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png", "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/132.png"], "stats": {"hp": 48, "attack": 48, "defense": 48, "special-attack": 48, "special-defense": 48, "speed": 48}, "types": ["normal"], "weight": 40}'
