from ast import literal_eval
from marshmallow import Schema, fields, validate, validates_schema, ValidationError


class POST(Schema):
    title = fields.Str(required=True,
                       validate=validate.Length(min=1, max=50))
    content = fields.Str(required=True,
                         validate=validate.Length(min=0, max=100))


class GET(Schema):
    titles = fields.Method(
        deserialize='validate_query_string_list')
    from_date = fields.DateTime(
        required=False, format='%Y-%m-%d %H:%M:%S')
    to_date = fields.DateTime(
        required=False, format='%Y-%m-%d %H:%M:%S')
    page = fields.Int(
        required=False, validate=validate.Range(min=0))
    limit = fields.Int(
        required=False, validate=validate.Range(min=0))

    def validate_query_string_list(self, value):
        try:
            result = literal_eval(value)
            if type(result) is list:
                return result
            raise ValidationError(
                "The list doesn't have the correct format") from e
        except Exception as e:
            raise ValidationError(
                "The list doesn't have the correct format") from e

    @validates_schema
    def validate_dates(self, data: dict, **kwargs):
        from_date = data.get('from_date', None)
        to_date = data.get('to_date', None)
        if (from_date and not to_date) or (not from_date and to_date):
            raise ValidationError(
                message='Needs the two dates to make a search with range')


class PUT(Schema):
    id = fields.Str(required=True, validate=validate.Length(min=24, max=24))
    title = fields.Str(required=True,
                       validate=validate.Length(min=1, max=50))
    content = fields.Str(required=True,
                         validate=validate.Length(min=0, max=100))


class DELETE(Schema):
    id = fields.Str(required=True, validate=validate.Length(min=24, max=24))
