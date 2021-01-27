import json

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

from api import app, schemas, views


spec = APISpec(
    title="Poke-Query",
    version="1.0.0",
    openapi_version="3.0.2",
    info={"description": "API that adds query improvements to the great PokéAPI"},
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

spec.components.schema("PokemonList", schema=schemas.PokemonListSchema)
spec.components.schema("PokemonData", schema=schemas.PokemonDataSchema)
spec.components.schema("ErrorData", schema=schemas.ErrorDataSchema)

with app.test_request_context():
    spec.path(view=views.pokemon_search)
    spec.path(view=views.pokemon_detail)

with open("api/static/swagger.json", "w") as f:
    json.dump(spec.to_dict(), f)
