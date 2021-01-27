import json

import pytest
import redis

from api import app, service
from tests.api.fixtures.data import DATA_KEYS, POKEMON_LIST, POKEMON_DATA_CACHED
from tests.api.mocks import MockRedis


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def mock_redis_client(monkeypatch):
    mock_redis_client = MockRedis()
    monkeypatch.setattr(redis, "Redis", mock_redis_client)
    return mock_redis_client


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


def test_pokemon_detail(monkeypatch, client):
    def get_pokemon_data(*args, **kwargs):
        return json.loads(POKEMON_DATA_CACHED)

    monkeypatch.setattr(service, "get_pokemon_data", get_pokemon_data)

    response = client.get("/ditto")
    data = json.loads(response.data)

    assert list(data.keys()) == DATA_KEYS
    assert data["id"] == 132
    assert data["name"] == "ditto"


def test_pokemon_detail_incorrect_name(monkeypatch, client):
    def get_pokemon_data(*args, **kwargs):
        return None

    monkeypatch.setattr(service, "get_pokemon_data", get_pokemon_data)

    response = client.get("/asd")
    assert response.status_code == 404


def test_docs_page_loads(client):
    response = client.get("/docs", follow_redirects=True)
    assert b"Swagger UI" in response.data
