import json
import os

import redis
import requests

from api.constants import POKEAPI_BASE_URL


def get_pokemons() -> dict:
    """Get all pokémon names from PokéAPI service. Will attempt to retrieve from cache first"""
    cache = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379)
    if cached_data := cache.get("pokemon-list"):
        return json.loads(cached_data)

    response = requests.get(f"{POKEAPI_BASE_URL}/pokemon?limit=1500")
    if response.ok:
        data = response.json()
        cache.set("pokemon-list", json.dumps(data["results"]))

        return data["results"]


def get_pokemon_data(pokemon_name: str) -> dict:
    """Get pokémon information from PokéAPI service. Will attempt to retrieve from cache first"""
    cache = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379)
    if cached_data := cache.get(pokemon_name):
        return json.loads(cached_data)

    response = requests.get(f"{POKEAPI_BASE_URL}/pokemon/{pokemon_name}")
    if response.ok:
        data = response.json()
        parsed_data = {
            "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            "base_experience": data["base_experience"],
            "forms": [form["name"] for form in data["forms"]],
            "height": data["height"],
            "id": data["id"],
            "location_area_encounters": data["location_area_encounters"],
            "moves": [move["move"]["name"] for move in data["moves"]],
            "name": data["name"],
            "order": data["order"],
            "species": data["species"]["name"],
            "sprites": [
                data["sprites"][sprite]
                for sprite in data["sprites"]
                if data["sprites"][sprite] and isinstance(data["sprites"][sprite], str)
            ],
            "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
            "types": [t["type"]["name"] for t in data["types"]],
            "weight": data["weight"],
        }

        cache.set(pokemon_name, json.dumps(parsed_data))
        return parsed_data
