from unittest.mock import Mock

import requests
import redis

from api.service import get_pokemons


MOCK_RESPONSE_DICT = {
    "count": 5,
    "next": None,
    "previous": None,
    "results": [
        {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
        {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"},
        {"name": "venusaur", "url": "https://pokeapi.co/api/v2/pokemon/3/"},
        {"name": "charmander", "url": "https://pokeapi.co/api/v2/pokemon/4/"},
        {"name": "charmeleon", "url": "https://pokeapi.co/api/v2/pokemon/5/"},
    ],
}

MOCK_RESPONSE_JSON = '[{"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"}, {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}, {"name": "venusaur", "url": "https://pokeapi.co/api/v2/pokemon/3/"}, {"name": "charmander", "url": "https://pokeapi.co/api/v2/pokemon/4/"}, {"name": "charmeleon", "url": "https://pokeapi.co/api/v2/pokemon/5/"}]'


class MockRequests:
    class MockResponse:
        def __init__(self, ok=True, json_data=None):
            self.ok = ok
            self.json_method_called = False
            self.json_data = json_data

        def json(self):
            self.json_method_called = True
            return self.json_data

    def __init__(self, ok=True, json_data=None):
        self.ok = ok
        self.json_data = json_data
        self.get_method_called = False

    def __call__(self, *args, **kwargs):
        self.get_method_called = True
        self.response = self.__class__.MockResponse(json_data=self.json_data)
        return self.response


class MockRedis:
    def __init__(self, get_data=None):
        self.get_data = get_data
        self.get_method_called = False
        self.set_method_called = False

    def get(self, *args, **kwargs):
        self.get_method_called = True
        return self.get_data

    def set(self, *args, **kwargs):
        self.set_method_called = True

    def __call__(self, *args, **kwargs):
        return self


def test_get_pokemons_no_cache(monkeypatch):
    mock_redis_client = MockRedis()
    mock_requests_get = MockRequests(json_data=MOCK_RESPONSE_DICT)

    monkeypatch.setattr(redis, "Redis", mock_redis_client)
    monkeypatch.setattr(requests, "get", mock_requests_get)

    pokemons = get_pokemons()

    assert mock_redis_client.get_method_called
    assert mock_redis_client.set_method_called
    assert mock_requests_get.get_method_called
    assert mock_requests_get.response.json_method_called
    assert len(pokemons) == 5


def test_get_pokemons_cached(monkeypatch):
    mock_redis_client = MockRedis(get_data=MOCK_RESPONSE_JSON)
    mock_requests_get = MockRequests()

    monkeypatch.setattr(redis, "Redis", mock_redis_client)
    monkeypatch.setattr(requests, "get", mock_requests_get)

    pokemons = get_pokemons()

    assert mock_redis_client.get_method_called
    assert not mock_redis_client.set_method_called
    assert not mock_requests_get.get_method_called
    assert len(pokemons) == 5
