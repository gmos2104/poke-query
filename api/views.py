from flask import abort, jsonify, request, Response, render_template

from api import app
from api.constants import POKEAPI_BASE_URL
from api.service import get_pokemons, get_pokemon_data
from api.utils import extract_id, get_sprite_url


def make_error_response(status_code: int, extra_data: dict) -> Response:
    response = jsonify(extra_data)
    response.status_code = status_code

    return response


@app.route("/", methods=["GET"])
def pokemon_search() -> Response:
    """Pokémon list view.
    ---
    get:
        description: Get pokémon names
        parameters:
        - in: query
          name: q
          required: false
          description: filter results based on name
        - in: query
          name: offset
          required: false
        - in: query
          name: limit
          required: false
        responses:
            200:
                content:
                    application/json:
                        schema: PokemonList
    """
    pokemons = get_pokemons()

    if q := request.args.get("q"):
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
    """Pokémon detail view.
    ---
    get:
        description: Get Pokémon data
        parameters:
        - in: path
          name: name
          description: full pokémon name
        responses:
            200:
                content:
                    application/json:
                        schema: PokemonData
            404:
                content:
                    application/json:
                        schema: ErrorData
    """
    if data := get_pokemon_data(name):
        return jsonify(data)

    return make_error_response(
        404,
        {
            "message": f"No Pokemon found with name {name}. Make sure you typed the name correctly."
        },
    )


@app.route("/docs/", methods=["GET"])
def swagger_docs():
    return render_template("index.html")
