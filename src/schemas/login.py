from marshmallow import Schema, fields, validate


class POST(Schema):
    email = fields.Email(required=True,
                         validate=validate.Length(max=50))
    password = fields.Str(required=True,
                          validate=validate.Length(min=8))
