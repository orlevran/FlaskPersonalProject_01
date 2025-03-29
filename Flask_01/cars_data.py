import json
import uuid

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

class CarItem:
    def __init__(self, make, model, year, engine, transmission, fuel_efficiency, dimensions, features, price):
        self._id = uuid.uuid4().hex
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
            "_id" : self._id,
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
    

car1 = CarItem(
    make="Toyota",
    model="Camry",
    year=2022,
    engine={
          "fuel_type" : "Gasoline",
          "displacement" : "2.5L",
          "horsepower" : 203,
          "torque" : "184 lb-ft"
    },
    transmission="8-speed Automatic",
    fuel_efficiency={"city_mpg" : 28, "highway_mpg" : 39},
    dimensions={"length" : "192.1 in", "width" : "72.4 in in", "height" : "56.9 in", "wheelbase" : "111.2 in"},
    features=["Apple CarPlay","Android Auto","Adaptive Cruise Control","Lane Departure Warning"],
    price=25995)

car2 = CarItem(
    make="Honda",
    model="Civic",
    year=2023,
    engine={
          "fuel_type" : "Turbocharged Gasoline",
          "displacement" : "1.5L",
          "horsepower" : 180,
          "torque" : "177 lb-ft"
    },
    transmission="CVT",
    fuel_efficiency={"city_mpg" : 31, "highway_mpg" : 40},
    dimensions={"length" : "184.0 in", "width" : "70.9 in", "height" : "56.9 in", "wheelbase" : "111.2 in"},
    features=["Wireless Apple CarPlay","Honda Sensing Safety Suite","Heated Front Seats","Blind Spot Monitoring"],
    price=24900)

"""
car3 = Car(
    make="Ford",
    model="Mustang",
    year=2024,
    engine={
          "fuel_type" : "V8",
          "displacement" : "5.0L",
          "horsepower" : 450,
          "torque" : "410 lb-ft"
    },
    transmission="6-speed Manual",
    fuel_efficiency={"city_mpg" : 15, "highway_mpg" : 24},
    dimensions={"length" : "188.5 in", "width" : "75.4 in", "height" : "54.3 in", "wheelbase" : "107.1 in"},
    features=["Performance Exhaust","Track Mode","Leather Interior","B&O Sound System"],
    price=43000)
    """

cars = {
    str(car1._id) : car1.to_dict(), str(car2._id) : car2.to_dict()
    #, 3 : car3.to_dict()
}