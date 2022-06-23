from marshmallow import Schema, fields


class MovieSchema(Schema):
    id = fields.Integer()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Integer()
    rating = fields.Float()
    genre_id = fields.Integer()
    genre = fields.Str()
    director_id = fields.Integer()
    director = fields.Str()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
