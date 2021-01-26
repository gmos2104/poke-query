import json
import os

import redis
import requests

from api.constants import POKEAPI_BASE_URL


def get_pokemons():
    cache = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379)
    cached_data = cache.get("pokemon-list")
    if cached_data:
        return json.loads(cached_data)

    response = requests.get(f"{POKEAPI_BASE_URL}/pokemon?limit=1500")
    if response.ok:
        data = response.json()
        cache.set("pokemon-list", json.dumps(data["results"]))

    return data["results"]
