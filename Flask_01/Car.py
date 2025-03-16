import json

class Engine:
    def __init__(self, fuel_type, displacement, horsepower, torque):
        self.fuel_type = fuel_type
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque

    def __repr__(self):
        return f"Engine(fuel_type={self.fuel_type}, displacement={self.displacement}, horsepower={self.horsepower}, torque={self.torque})"
    
    def to_dict(self):
        return {
            "fuel_type": self.fuel_type,
            "displacement": self.displacement,
            "horsepower": self.horsepower,
            "torque": self.torque
        }

class FuelEfficiency:
    def __init__(self, city_mpg, highway_mpg):
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg

    def __repr__(self):
        return f"FuelEfficiency(city_mpg={self.city_mpg}, highway_mpg={self.highway_mpg})"
    
    def to_dict(self):
        return {
            "city_mpg": self.city_mpg,
            "highway_mpg": self.highway_mpg
        }

class Dimensions:
    def __init__(self, length, width, height, wheelbase):
        self.length = length
        self.width = width
        self.height = height
        self.wheelbase = wheelbase

    def __repr__(self):
        return f"Dimensions(length={self.length}, width={self.width}, height={self.height}, wheelbase={self.wheelbase})"
    
    def to_dict(self):
        return {
            "length": self.length,
            "width": self.width,
            "height": self.height,
            "wheelbase": self.wheelbase
        }

class Car:
    def __init__(self, make, model, year, engine, transmission, fuel_efficiency, dimensions, features, price):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(**engine)
        self.transmission = transmission
        self.fuel_efficiency = FuelEfficiency(**fuel_efficiency)
        self.dimensions = Dimensions(**dimensions)
        self.features = features
        self.price = price

    def __repr__(self):
        return (f"Car(make={self.make}, model={self.model}, year={self.year}, engine={self.engine}, "
                f"transmission={self.transmission}, fuel_efficiency={self.fuel_efficiency}, "
                f"dimensions={self.dimensions}, features={self.features}, price={self.price})")
    
    def to_dict(self):
        return {
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "engine": self.engine.to_dict(),
            "transmission": self.transmission,
            "fuel_efficiency": self.fuel_efficiency.to_dict(),
            "dimensions": self.dimensions.to_dict(),
            "features": self.features,
            "price": self.price
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
