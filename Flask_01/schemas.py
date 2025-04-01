from marshmallow import Schema, fields, validate

class EngineSchema(Schema):
    fuel_type = fields.Str(required=True)
    displacement = fields.Str(required=True)
    horsepower = fields.Int(required=True)
    torque = fields.Str(required=True)

class EngineUpdateSchema(Schema):
    fuel_type = fields.Str()
    displacement = fields.Str()
    horsepower = fields.Int()
    torque = fields.Str()
    # Optional fields for partial updates

class FuelEfficiencySchema(Schema):
    city_mpg = fields.Int(required=True)
    highway_mpg = fields.Int(required=True)

class FuelEfficiencyUpdateSchema(Schema):
    city_mpg = fields.Int()
    highway_mpg = fields.Int()
    # Optional fields for partial updates

class DimensionsSchema(Schema):
    length = fields.Str(required=True)
    width = fields.Str(required=True)
    height = fields.Str(required=True)
    wheelbase = fields.Str(required=True)

class DimensionsUpdateSchema(Schema):
    length = fields.Str()
    width = fields.Str()
    height = fields.Str()
    wheelbase = fields.Str()
    # Optional fields for partial updates

class CarSchema(Schema):
    _id = fields.Str(dump_only=True)  # Read-only field for the car's unique ID
    make = fields.Str(required=True)
    model = fields.Str(required=True)
    year = fields.Int(required=True)
    engine = fields.Nested(EngineSchema, required=True)
    transmission = fields.Str(required=True)
    fuel_efficiency = fields.Nested(FuelEfficiencySchema, required=True)
    dimensions = fields.Nested(DimensionsSchema, required=True)
    features = fields.List(fields.Str(), required=True)
    price = fields.Float(required=True)

class CarUpdateSchema(Schema):
    make = fields.Str()
    model = fields.Str()
    year = fields.Int()
    engine = fields.Nested(EngineSchema)
    transmission = fields.Str()
    fuel_efficiency = fields.Nested(FuelEfficiencySchema)
    dimensions = fields.Nested(DimensionsSchema)
    features = fields.List(fields.Str())
    price = fields.Float()
    # Define the fields that can be updated
    # Optional fields for partial updates