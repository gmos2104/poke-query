from flask import jsonify, request, Response

from api import app
from api.constants import POKEAPI_BASE_URL
from api.service import get_pokemons
from api.utils import extract_id, get_sprite_url


@app.route("/", methods=["GET"])
def pokemon_search() -> Response:
    pokemons = get_pokemons()

    q = request.args.get("q")
    if q:
        pokemons = [p for p in pokemons if q.lower() in p["name"].lower()]

    count = len(pokemons)
    limit = int(request.args.get("limit", 10))
    offset = int(request.args.get("offset", 0))

    data = []
    for pokemon in pokemons[offset : limit + offset]:
        pokemon_id = extract_id(pokemon["url"])
        data.append(
            {
                "id": pokemon_id,
                "name": pokemon["name"],
                "image": get_sprite_url(pokemon_id),
            }
        )

    return jsonify(
        {
            "count": count,
            "limit": limit,
            "offset": offset,
            "data": data,
        }
    )


@app.route("/<name>", methods=["GET"])
def pokemon_detail(name: str) -> Response:
    return jsonify({"message": f"Stats for {name}"})
