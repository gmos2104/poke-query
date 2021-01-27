import requests
import redis

from api.service import get_pokemons, get_pokemon_data
from tests.api.fixtures.data import (
    DATA_KEYS,
    POKEMON_LIST_RESPONSE,
    POKEMON_LIST_CACHED,
    POKEMON_DATA_RESPONSE,
    POKEMON_DATA_CACHED,
)
from tests.api.mocks import MockRequests, MockRedis


def test_get_pokemons_no_cache(monkeypatch):
    mock_redis_client = MockRedis()
    mock_requests_get = MockRequests(json_data=POKEMON_LIST_RESPONSE)

    monkeypatch.setattr(redis, "Redis", mock_redis_client)
    monkeypatch.setattr(requests, "get", mock_requests_get)

    pokemons = get_pokemons()

    assert mock_redis_client.get_method_called
    assert mock_redis_client.set_method_called
    assert mock_requests_get.get_method_called
    assert mock_requests_get.response.json_method_called
    assert len(pokemons) == 5


def test_get_pokemons_cached(monkeypatch):
    mock_redis_client = MockRedis(get_data=POKEMON_LIST_CACHED)
    mock_requests_get = MockRequests()

    monkeypatch.setattr(redis, "Redis", mock_redis_client)
    monkeypatch.setattr(requests, "get", mock_requests_get)

    pokemons = get_pokemons()

    assert mock_redis_client.get_method_called
    assert not mock_redis_client.set_method_called
    assert not mock_requests_get.get_method_called
    assert len(pokemons) == 5


def test_get_pokemon_data_no_cache(monkeypatch):
    mock_redis_client = MockRedis()
    mock_requests_get = MockRequests(json_data=POKEMON_DATA_RESPONSE)

    monkeypatch.setattr(redis, "Redis", mock_redis_client)
    monkeypatch.setattr(requests, "get", mock_requests_get)

    data = get_pokemon_data("ditto")
    assert mock_redis_client.get_method_called
    assert mock_redis_client.set_method_called
    assert mock_requests_get.get_method_called
    assert mock_requests_get.response.json_method_called
    assert list(data.keys()) == DATA_KEYS
    assert data["id"] == 132
    assert data["name"] == "ditto"


def test_get_pokemon_data_cached(monkeypatch):
    mock_redis_client = MockRedis(get_data=POKEMON_DATA_CACHED)
    mock_requests_get = MockRequests()

    monkeypatch.setattr(redis, "Redis", mock_redis_client)
    monkeypatch.setattr(requests, "get", mock_requests_get)

    data = get_pokemon_data("ditto")
    assert mock_redis_client.get_method_called
    assert not mock_redis_client.set_method_called
    assert not mock_requests_get.get_method_called
    assert list(data.keys()) == DATA_KEYS
    assert data["id"] == 132
    assert data["name"] == "ditto"
