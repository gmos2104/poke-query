from marshmallow import Schema, fields


class PokemonListItemSchema(Schema):
    id = fields.Int()
    name = fields.String()
    image = fields.String()


class PokemonListSchema(Schema):
    count = fields.Int()
    limit = fields.String()
    offset = fields.String()
    data = fields.List(fields.Nested(PokemonListItemSchema))


class StatsSchema(Schema):
    attack = fields.Int()
    defense = fields.Int()
    hp = fields.Int()
    special_attack = fields.Int(data_key="special-attack")
    special_defense = fields.Int(data_key="special-defense")
    speed = fields.Int()


class PokemonDataSchema(Schema):
    abilities = fields.List(fields.String())
    base_experience = fields.Int()
    forms = fields.List(fields.String())
    height = fields.Int()
    id = fields.Int()
    location_area_encounters = fields.String()
    moves = fields.List(fields.String())
    name = fields.String()
    order = fields.Int()
    species = fields.String()
    sprites = fields.List(fields.String())
    stats = fields.Nested(StatsSchema)
    types = fields.List(fields.String())
    weight = fields.Int()


class ErrorDataSchema(Schema):
    message = fields.String()
