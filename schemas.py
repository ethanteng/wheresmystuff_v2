from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    id = fields.Str(dump_only=True)
    email = fields.Str(required=True)
    first_name = fields.Str()
    last_name = fields.Str()


class PlainPackageSchema(Schema):
    id = fields.Str(dump_only=True)
    tracking_code = fields.Str(required=True)
    carrier = fields.Str()
    description = fields.Str()
    custom_url = fields.Str()


class UserSchema(PlainUserSchema):
    packages = fields.List(fields.Nested(PlainPackageSchema()), dump_only=True)


class PackageSchema(PlainPackageSchema):
    email = fields.Str(required=True, load_only=True)
    user = fields.Nested(PlainUserSchema(), dump_only=True)