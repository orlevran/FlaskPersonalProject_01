from marshmallow import Schema, fields, validate

class TorqueSchema(Schema):
    torque_value = fields.Int(required=True)
    rpm = fields.Int(required=True)
    value = fields.Str(required=True)

class TorqueUpdateSchema(Schema):
    torque_value = fields.Int()
    unit = fields.Str()
    rpm = fields.Int()

class EngineSchema(Schema):
    engine_type = fields.Str(required=True)
    fuel_type = fields.Str(required=True)
    displacement = fields.Str(required=True)
    horsepower = fields.Int(required=True)
    torque = fields.Nested(TorqueSchema, required=True)
    aspiration = fields.Str(required=True)

class EngineUpdateSchema(Schema):
    engine_type = fields.Str()
    fuel_type = fields.Str()
    displacement = fields.Str()
    horsepower = fields.Int()
    torque = fields.Nested(TorqueSchema)
    aspiration = fields.Str()

class TransmissionSchema(Schema):
    transmission_type = fields.Str(required=True)
    number_of_gears = fields.Int(required=True)
    description = fields.Str(required=True)

class TransmissionUpdateSchema(Schema):
    transmission_type = fields.Str()
    number_of_gears = fields.Int()
    description = fields.Str()

class FuelEfficiencySchema(Schema):
    city_mpg = fields.Int(required=True)
    highway_mpg = fields.Int(required=True)
    combined_mpg = fields.Int(required=True)

class FuelEfficiencyUpdateSchema(Schema):
    city_mpg = fields.Int()
    highway_mpg = fields.Int()
    combined_mpg = fields.Int()

class DimensionsUnitSchema(Schema):
    unit = fields.Str(required=True)
    value = fields.Str(required=True)
    # Define the unit of measurement for dimensions
    # e.g., "inches", "cm", etc.

class DimensionsUnitUpdateSchema(Schema):
    unit = fields.Str()
    value = fields.Str()
    # Optional fields for partial updates
    # Define the unit of measurement for dimensions
    # e.g., "inches", "cm", etc.

class DimensionsSchema(Schema):
    length = fields.Nested(DimensionsUnitSchema, required=True)
    width = fields.Nested(DimensionsUnitSchema, required=True)
    height = fields.Nested(DimensionsUnitSchema, required=True)
    wheelbase = fields.Nested(DimensionsUnitSchema, required=True)
    curb_weight = fields.Nested(DimensionsUnitSchema, required=True)
    # Define the dimensions of the car
    # e.g., length, width, height, wheelbase

class DimensionsUpdateSchema(Schema):
    length = fields.Nested(DimensionsUnitSchema)
    width = fields.Nested(DimensionsUnitSchema)
    height = fields.Nested(DimensionsUnitSchema)
    wheelbase = fields.Nested(DimensionsUnitSchema)
    curb_weight = fields.Nested(DimensionsUnitSchema)
    # Optional fields for partial updates
    # Define the dimensions of the car
    # e.g., length, width, height, wheelbase

class FeaturesSchema(Schema):
    infotainment = fields.List(fields.Str(), required=True)
    safety = fields.List(fields.Str(), required=True)
    comfort = fields.List(fields.Str(), required=True)

class FeaturesUpdateSchema(Schema):
    infotainment = fields.List(fields.Str())
    safety = fields.List(fields.Str())
    comfort = fields.List(fields.Str())
    # Optional fields for partial updates
    # Define the features of the car
    # e.g., infotainment, safety, comfort

class PriceSchema(Schema):
    base_price = fields.Float(required=True)
    currency = fields.Str(required=True)
    msrp = fields.Float(required=True)
    destination_fee = fields.Float(required=True)
    total_price = fields.Float(required=True)

class PriceUpdateSchema(Schema):
    base_price = fields.Float()
    currency = fields.Str()
    msrp = fields.Float()
    destination_fee = fields.Float()
    total_price = fields.Float()
    # Optional fields for partial updates
    # Define the price details of the car
    # e.g., base price, currency, MSRP, destination fee, total price

class WarrantyUnitSchema(Schema):
    duration_years = fields.Str(required=True)
    miles = fields.Str(required=True)
    # Define the unit of measurement for warranty
    # e.g., "years", "miles", etc.

class WarrantyUnitUpdateSchema(Schema):
    duration_years = fields.Str()
    miles = fields.Str()
    # Optional fields for partial updates
    # Define the unit of measurement for warranty
    # e.g., "years", "miles", etc.

class WarrantySchema(Schema):
    basic = fields.Nested(WarrantyUnitSchema, required=True)
    powertrain = fields.Nested(WarrantyUnitSchema, required=True)
    roadside_assistance = fields.Nested(WarrantyUnitSchema, required=True)

class WarrantyUpdateSchema(Schema):
    basic = fields.Nested(WarrantyUnitSchema)
    powertrain = fields.Nested(WarrantyUnitSchema)
    roadside_assistance = fields.Nested(WarrantyUnitSchema)
    # Optional fields for partial updates
    # Define the warranty details of the car
    # e.g., basic, powertrain, roadside assistance

class CarSchema(Schema):
    _id = fields.Str(dump_only=True)  # Read-only field for the car's unique ID
    make = fields.Str(required=True)
    model = fields.Str(required=True)
    year = fields.Int(required=True)
    engine = fields.Nested(EngineSchema, required=True)
    transmission = fields.Nested(TransmissionSchema, required=True)
    drivetrain = fields.Str(required=True)
    fuel_efficiency = fields.Nested(FuelEfficiencySchema, required=True)
    dimensions = fields.Nested(DimensionsSchema, required=True)
    features = fields.Nested(FeaturesSchema, required=True)
    color_options = fields.List(fields.Str(), required=True)
    price = fields.Nested(PriceSchema, required=True)
    warranty = fields.Nested(WarrantySchema, required=True)

class CarUpdateSchema(Schema):
    make = fields.Str()
    model = fields.Str()
    year = fields.Int()
    engine = fields.Nested(EngineSchema)
    transmission = fields.Nested(TransmissionSchema)
    drivetrain = fields.Str()
    fuel_efficiency = fields.Nested(FuelEfficiencySchema)
    dimensions = fields.Nested(DimensionsSchema)
    features = fields.Nested(FeaturesSchema.Str())
    color_options = fields.List(fields.Str())
    price = fields.Nested(PriceSchema)
    warranty = fields.Nested(WarrantySchema)
    # Define the fields that can be updated
    # Optional fields for partial updates