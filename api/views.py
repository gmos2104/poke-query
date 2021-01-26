from flask import jsonify

from api import app


@app.route("/", methods=["GET"])
def pokemon_search():
    return jsonify({"message": f"List of Pokémons"})


@app.route("/<name>", methods=["GET"])
def pokemon_detail(name):
    return jsonify({"message": f"Stats for {name}"})
