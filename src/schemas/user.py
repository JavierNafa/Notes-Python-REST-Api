from marshmallow import Schema, fields, validate


class POST(Schema):
    name = fields.Str(required=True,
                      validate=validate.Length(min=3, max=25))
    last_name = fields.Str(required=True,
                           validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True,
                         validate=validate.Length(max=50))
    password = fields.Str(required=True,
                          validate=validate.Length(min=8))
