import pytest

from api.utils import extract_id, get_sprite_url


@pytest.mark.parametrize(
    "url, expected_id",
    [
        ("https://pokeapi.co/api/v2/pokemon/1/", 1),
        ("https://pokeapi.co/api/v2/pokemon/124/", 124),
        ("https://pokeapi.co/api/v2/pokemon/452/", 452),
    ],
)
def test_extract_id(url, expected_id):
    assert extract_id(url) == expected_id


@pytest.mark.parametrize(
    "pokemon_id, expected_sprite_url",
    [
        (
            1,
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        ),
        (
            124,
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/124.png",
        ),
        (
            452,
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/452.png",
        ),
    ],
)
def test_get_sprite_url(pokemon_id, expected_sprite_url):
    assert get_sprite_url(pokemon_id) == expected_sprite_url
