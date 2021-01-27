from .constants import POKEAPI_SPRITE_BASE


def extract_id(url: str) -> int:
    """Get Pokémon ID from the URL"""
    return int(url.split("/")[-2])


def get_sprite_url(pokemon_id: int) -> str:
    """Get sprite absolute URL for given ID"""
    return f"{POKEAPI_SPRITE_BASE}/{pokemon_id}.png"
