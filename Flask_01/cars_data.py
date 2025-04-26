import json
import uuid

    
class Engine:
    def __init__(self, engine_type, fuel_type, displacement, horsepower, torque, aspiration):
        self.engine_type = engine_type
        self.fuel_type = fuel_type
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque
        self.aspiration = aspiration

    def __repr__(self):
        return (f"Engine(engine_type={self.engine_type}, fuel_type={self.fuel_type}, "
                f"displacement={self.displacement}, horsepower={self.horsepower}, "
                f"torque={self.torque}, aspiration={self.aspiration})")
    
    def to_dict(self):
        return {
            "engine_type": self.engine_type,
            "fuel_type": self.fuel_type,
            "displacement": self.displacement,
            "horsepower": self.horsepower,
            "torque": self.torque.to_dict() if isinstance(self.torque, Torque) else self.torque,
            "aspiration": self.aspiration
        }

class Torque:
    def __init__(self, torque_value, unit, rpm):
        self.torque_value = torque_value
        self.unit = unit
        self.rpm = rpm

    def __repr__(self):
        return f"Torque(torque_value={self.torque_value}, unit={self.unit}, rpm={self.rpm})"
    
    def to_dict(self):
        return {
            "torque_value": self.torque_value,
            "unit": self.unit,
            "rpm": self.rpm
        }

class Transmission:
    def __init__(self, transmission_type, gears, description):
        self.transmission_type = transmission_type
        self.gears = gears
        self.description = description

    def __repr__(self):
        return (f"Transmission(transmission_type={self.transmission_type}, "
                f"gears={self.gears}, description={self.description})")
    
    def to_dict(self):
        return {
            "transmission_type": self.transmission_type,
            "gears": self.gears,
            "description": self.description
        }

class FuelEfficiency:
    def __init__(self, city_mpg, highway_mpg, combined_mpg):
        self.city_mpg = city_mpg
        self.highway_mpg = highway_mpg
        self.combined_mpg = combined_mpg

    def __repr__(self):
        return (f"FuelEfficiency(city_mpg={self.city_mpg}, highway_mpg={self.highway_mpg}, combined_mpg={self.combined_mpg})")
    
    def to_dict(self):
        return {
            "city_mpg": self.city_mpg,
            "highway_mpg": self.highway_mpg,
            "combined_mpg": self.combined_mpg
        }

class Dimensions:
    def __init__(self, length, width, height, wheelbase, curb_weight):
        self.length = length
        self.width = width
        self.height = height
        self.wheelbase = wheelbase
        self.curb_weight = curb_weight

    def __repr__(self):
        return (f"Dimensions(length={self.length}, width={self.width}, "
                f"height={self.height}, wheelbase={self.wheelbase}, curb_weight={self.curb_weight})")
    
    def to_dict(self):
        return {
            "length": self.length.to_dict() if isinstance(self.length, DimensionsUnit) else self.length,
            "width": self.width.to_dict() if isinstance(self.width, DimensionsUnit) else self.width,
            "height": self.height.to_dict() if isinstance(self.height, DimensionsUnit) else self.height,
            "wheelbase": self.wheelbase.to_dict() if isinstance(self.wheelbase, DimensionsUnit) else self.wheelbase,
            "curb_weight": self.curb_weight.to_dict() if isinstance(self.curb_weight, DimensionsUnit) else self.curb_weight
        }
    
class DimensionsUnit:
    def __init__(self, unit_value, unit_name):
        self.unit_value = unit_value
        self.unit_name = unit_name

    def __repr__(self):
        return (f"DimensionsUnit(unit_value={self.unit_value}, unit_name={self.unit_name})")
    
    def to_dict(self):
        return {
            "unit_value": self.unit_value,
            "unit_name": self.unit_name
        }

class Features:
    def __init__(self,infotainment, safety, comfort):
        self.infotainment = infotainment
        self.safety = safety
        self.comfort = comfort

    def __repr__(self):
        return (f"Features(infotainment={self.infotainment}, safety={self.safety}, "
                f"comfort={self.comfort})")
    
    def to_dict(self):
        return {
            "infotainment": self.infotainment.to_dict() if isinstance(self.infotainment, list) else self.infotainment,
            "safety": self.safety.to_dict() if isinstance(self.safety, list) else self.safety,
            "comfort": self.comfort.to_dict() if isinstance(self.comfort, list) else self.comfort
        }

class Price:
    def __init__(self, base_price, currency, msrp, destination_fee, total_price):
        self.base_price = base_price
        self.currency = currency
        self.msrp = msrp
        self.destination_fee = destination_fee
        self.total_price = total_price

    def __repr__(self):
        return (f"Price(base_price={self.base_price}, currency={self.currency}, "
                f"msrp={self.msrp}, destination_fee={self.destination_fee}, total_price={self.total_price})")
    
    def to_dict(self):
        return {
            "base_price": self.base_price,
            "currency": self.currency,
            "msrp": self.msrp,
            "destination_fee": self.destination_fee,
            "total_price": self.total_price
        }

class Warranty:
    def __init__(self, basic, powertrain, roadside_assistance):
        self.basic = basic
        self.powertrain = powertrain
        self.roadside_assistance = roadside_assistance

    def __repr__(self):
        return (f"Warranty(basic={self.basic}, powertrain={self.powertrain}, "
                f"roadside_assistance={self.roadside_assistance})")
    
    def to_dict(self):
        return {
            "basic": self.basic.to_dict() if isinstance(self.basic, WarrantyUnit) else self.basic,
            "powertrain": self.powertrain.to_dict() if isinstance(self.powertrain, WarrantyUnit) else self.powertrain,
            "roadside_assistance": self.roadside_assistance.to_dict() if isinstance(self.roadside_assistance, WarrantyUnit) else self.roadside_assistance
        }
    
class WarrantyUnit:
    def __init__(self, duration_years, miles):
        self.duration_years = duration_years
        self.miles = miles

    def __repr__(self):
        return (f"WarrantyUnit(duration_years={self.duration_years}, miles={self.miles})")
    
    def to_dict(self):
        return {
            "duration_years": self.duration_years,
            "miles": self.miles
        }

class CarItem:
    def __init__(self, make, model, year, engine, transmission, drivetrain, fuel_efficiency,
                 dimensions, features, color_options, price, warranty):
        self._id = uuid.uuid4().hex
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.fuel_efficiency = fuel_efficiency
        self.dimensions = dimensions
        self.features = features
        self.color_options = color_options
        self.price = price
        self.warranty = warranty

    def __repr__(self):
        return (f"Car(make={self.make}, model={self.model}, year={self.year}, engine={self.engine}, "
                f"transmission={self.transmission}, drivetrain={self.drivetrain}, fuel_efficiency={self.fuel_efficiency}, "
                f"dimensions={self.dimensions}, features={self.features}, color_options={self.color_options}, "
                f"price={self.price}, warranty={self.warranty})")
    
    def to_dict(self):
        return {
            "_id": self._id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "engine": self.engine.to_dict() if isinstance(self.engine, Engine) else self.engine,
            "transmission": self.transmission.to_dict() if isinstance(self.transmission, Transmission) else self.transmission,
            "drivetrain": self.drivetrain,
            "fuel_efficiency": self.fuel_efficiency.to_dict() if isinstance(self.fuel_efficiency, FuelEfficiency) else self.fuel_efficiency,
            "dimensions": self.dimensions.to_dict() if isinstance(self.dimensions, Dimensions) else self.dimensions,
            "features": self.features.to_dict() if isinstance(self.features, Features) else self.features,
            "color_options": self.color_options.to_dict() if isinstance(self.color_options, list) else self.color_options,
            "price": self.price.to_dict() if isinstance(self.price, Price) else self.price,
            "warranty": self.warranty.to_dict() if isinstance(self.warranty, Warranty) else self.warranty
        }

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