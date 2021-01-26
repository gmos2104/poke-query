import json

import pytest

from api import app, service

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


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_search_pokemon(monkeypatch, client):
    def get_pokemons():
        return POKEMON_LIST

    monkeypatch.setattr(service, "get_pokemons", get_pokemons)

    limit = 10
    for offset in [0, 10]:
        response = client.get(f"/?offset={offset}&limit={limit}")
        data = json.loads(response.data)

        assert len(data["data"]) == limit
        assert [pokemon["id"] for pokemon in data["data"]] == list(
            range(1 + offset, 11 + offset)
        )

    response = client.get(f"/?q=pidge")
    data = json.loads(response.data)

    assert len(data) == 4
    assert [pokemon["name"] for pokemon in data["data"]] == [
        "pidgey",
        "pidgeotto",
        "pidgeot",
        "pidgeot-mega",
    ]
