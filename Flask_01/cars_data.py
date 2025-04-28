import uuid
    
class Engine:
    def __init__(self, engine_type, fuel_type, displacement, horsepower, torque, aspiration):
        self.engine_type = engine_type #string
        self.fuel_type = fuel_type #string
        self.displacement = displacement #string
        self.horsepower = horsepower #int
        self.torque = torque #Torque
        self.aspiration = aspiration #string

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
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            engine_type=data["engine_type"],
            fuel_type=["fuel_type"],
            displacement=data["displacement"],
            horsepower=data["horsepower"],
            torque=Torque.from_dict(data["torque"]) if "torque" in data else None,
            aspiration=data["aspiration"]
        )

class Torque:
    def __init__(self, torque_value, unit, rpm):
        self.torque_value = torque_value #int
        self.unit = unit #string
        self.rpm = rpm #int

    def __repr__(self):
        return f"Torque(torque_value={self.torque_value}, unit={self.unit}, rpm={self.rpm})"
    
    def to_dict(self):
        return {
            "torque_value": self.torque_value,
            "unit": self.unit,
            "rpm": self.rpm
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            torque_value=data["torque_value"],
            unit=data["unit"],
            rpm=data["rpm"]
        )

class Transmission:
    def __init__(self, transmission_type, gears, description):
        self.transmission_type = transmission_type #string
        self.gears = gears #int
        self.description = description #string

    def __repr__(self):
        return (f"Transmission(transmission_type={self.transmission_type}, "
                f"gears={self.gears}, description={self.description})")
    
    def to_dict(self):
        return {
            "transmission_type": self.transmission_type,
            "gears": self.gears,
            "description": self.description
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            transmission_type = data["transmission_type"],
            gears = data["gears"],
            description = data["description"]
        )

class FuelEfficiency:
    def __init__(self, city_mpg, highway_mpg, combined_mpg):
        self.city_mpg = city_mpg #int
        self.highway_mpg = highway_mpg #int
        self.combined_mpg = combined_mpg #int

    def __repr__(self):
        return (f"FuelEfficiency(city_mpg={self.city_mpg}, highway_mpg={self.highway_mpg}, combined_mpg={self.combined_mpg})")
    
    def to_dict(self):
        return {
            "city_mpg": self.city_mpg,
            "highway_mpg": self.highway_mpg,
            "combined_mpg": self.combined_mpg
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            city_mpg=data["city_mpg"],
            highway_mpg=data["highway_mpg"],
            combined_mpg=data["combined_mpg"]
        )

class Dimensions:
    def __init__(self, length, width, height, wheelbase, curb_weight):
        self.length = length #DimensionsUnit
        self.width = width #DimensionsUnit
        self.height = height #DimensionsUnit
        self.wheelbase = wheelbase #DimensionsUnit
        self.curb_weight = curb_weight #DimensionsUnit

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
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            length=DimensionsUnit.from_dict(data["length"]) if "length" in data else None,
            width=DimensionsUnit.from_dict(data["width"]) if "width" in data else None,
            height=DimensionsUnit.from_dict(data["height"]) if "height" in data else None,
            wheelbase=DimensionsUnit.from_dict(data["wheelbase"]) if "wheelbase" in data else None,
            curb_weight=DimensionsUnit.from_dict(data["curb_weight"]) if "curb_weight" in data else None
        )
    
class DimensionsUnit:
    def __init__(self, unit_value, unit_name):
        self.unit_value = unit_value #float
        self.unit_name = unit_name #string

    def __repr__(self):
        return (f"DimensionsUnit(unit_value={self.unit_value}, unit_name={self.unit_name})")
    
    def to_dict(self):
        return {
            "unit_value": self.unit_value,
            "unit_name": self.unit_name
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            unit_value=data["unit_value"],
            unit_name=data["unit_name"]
        ) 

class Features:
    def __init__(self,infotainment, safety, comfort):
        self.infotainment = infotainment #list of strings
        self.safety = safety #list of strings
        self.comfort = comfort #list of strings

    def __repr__(self):
        return (f"Features(infotainment={self.infotainment}, safety={self.safety}, "
                f"comfort={self.comfort})")
    
    def to_dict(self):
        return {
            "infotainment": self.infotainment,
            "safety": self.safety,
            "comfort": self.comfort
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            infotainment=data["infotainment"],
            safety=data["safety"],
            comfort=data["comfort"]
        )

class Price:
    def __init__(self, base_price, currency, msrp, destination_fee, total_price):
        self.base_price = base_price #float
        self.currency = currency #string
        self.msrp = msrp #float
        self.destination_fee = destination_fee #float
        self.total_price = total_price #float

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
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            base_price=data["base_price"],
            currency=data["currency"],
            msrp=data["msrp"],
            destination_fee=data["destination_fee"],
            total_price=data["total_price"]
        )

class Warranty:
    def __init__(self, basic, powertrain, roadside_assistance):
        self.basic = basic #WarrantyUnit
        self.powertrain = powertrain #WarrantyUnit
        self.roadside_assistance = roadside_assistance #WarrantyUnit

    def __repr__(self):
        return (f"Warranty(basic={self.basic}, powertrain={self.powertrain}, "
                f"roadside_assistance={self.roadside_assistance})")
    
    def to_dict(self):
        return {
            "basic": self.basic.to_dict() if isinstance(self.basic, WarrantyUnit) else self.basic,
            "powertrain": self.powertrain.to_dict() if isinstance(self.powertrain, WarrantyUnit) else self.powertrain,
            "roadside_assistance": self.roadside_assistance.to_dict() if isinstance(self.roadside_assistance, WarrantyUnit) else self.roadside_assistance
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            basic=WarrantyUnit.from_dict(data["basic"]) if "basic" in data else None,
            powertrain=WarrantyUnit.from_dict(data["powertrain"]) if "powertrain" in data else None,
            roadside_assistance=WarrantyUnit.from_dict(data["roadside_assistance"]) if "roadside_assistance" in data else None
        )
    
class WarrantyUnit:
    def __init__(self, duration_years, miles):
        self.duration_years = duration_years #int
        self.miles = miles #int

    def __repr__(self):
        return (f"WarrantyUnit(duration_years={self.duration_years}, miles={self.miles})")
    
    def to_dict(self):
        return {
            "duration_years": self.duration_years,
            "miles": self.miles
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            duration_years=data["duration_years"],
            miles=data["miles"]
        )

class CarItem:
    def __init__(self, make, model, year, engine, transmission, drivetrain, fuel_efficiency,
                 dimensions, features, color_options, price, warranty):
        self._id = uuid.uuid4().hex
        self.make = make #string
        self.model = model #string
        self.year = year #int
        self.engine = engine #Engine
        self.transmission = transmission #Transmission
        self.drivetrain = drivetrain #string
        self.fuel_efficiency = fuel_efficiency #FuelEfficiency
        self.dimensions = dimensions #Dimensions
        self.features = features #Features
        self.color_options = color_options #list of strings
        self.price = price #Price
        self.warranty = warranty #Warranty

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
            "color_options": self.color_options,
            "price": self.price.to_dict() if isinstance(self.price, Price) else self.price,
            "warranty": self.warranty.to_dict() if isinstance(self.warranty, Warranty) else self.warranty
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            make=data["make"],
            model=data["model"],
            year=data["year"],
            engine=Engine.from_dict(data["engine"]) if data.get("engine") else None,
            transmission=Transmission.from_dict(data["transmission"]) if data.get("transmission") else None,
            drivetrain=data["drivetrain"],
            fuel_efficiency=FuelEfficiency.from_dict(data["fuel_efficiency"]) if data.get("fuel_efficiency") else None,
            dimensions=Dimensions.from_dict(data["dimensions"]) if data.get("dimensions") else None,
            features=Features.from_dict(data["features"]) if data.get("features") else None,
            color_options=data.get("color_options", []),
            price=Price.from_dict(data["price"]) if data.get("price") else None,
            warranty=Warranty.from_dict(data["warranty"]) if data.get("warranty") else None
        )

car1 = CarItem(
    make = "Toyota",
    model = "Camry",
    year = 2022,
    engine= Engine(
        engine_type = "Inline-4",
        fuel_type = "Gasoline",
        displacement = "2.5L",
        horsepower = 203,
        torque = Torque(
            torque_value = 184,
            unit = "lb-ft",
            rpm = 5000
        ),
        aspiration = "Naturally Aspirated"
    ),
    transmission= Transmission(
        transmission_type = "Automatic",
        gears = 8,
        description = "8-Speed Automatic"
    ),
    drivetrain = "FWD",
    fuel_efficiency= FuelEfficiency(
        city_mpg = 28,
        highway_mpg = 39,
        combined_mpg = 32
    ),
        dimensions=Dimensions(
        length=DimensionsUnit(192.1, "inches"),
        width=DimensionsUnit(72.4, "inches"),
        height=DimensionsUnit(56.9, "inches"),
        wheelbase=DimensionsUnit(111.2, "inches"),
        curb_weight=DimensionsUnit(3241, "lbs")
    ),
    features= Features(
        infotainment = ["Apple CarPlay", "Android Auto", "Bluetooth"],
        safety = ["Adaptive Cruise Control", "Lane Keeping Assist"],
        comfort = ["Leather Seats", "Heated Front Seats"]
    ),
    color_options = ["White", "Black", "Silver", "Blue"],
    price= Price(
        base_price = 25000,
        currency = "USD",
        msrp = 25995,
        destination_fee = 995,
        total_price = 26990
    ),
    warranty= Warranty(
        basic = WarrantyUnit(
            duration_years = 3,
            miles = 36000
        ),
        powertrain = WarrantyUnit(
            duration_years = 5,
            miles = 60000
        ),
        roadside_assistance = WarrantyUnit(
            duration_years = 2,
            miles = "Unlimited"
        )
    )
)

car2 = CarItem(
    make="Ford",
    model="Mustang GT",
    year=2023,
    engine=Engine(
        engine_type="V8",
        fuel_type="Gasoline",
        displacement="5.0L",
        horsepower=450,
        torque=Torque(
            torque_value=410,
            unit="lb-ft",
            rpm=4600
        ),
        aspiration="Naturally Aspirated"
    ),
    transmission=Transmission(
        transmission_type="Manual",
        gears=6,
        description="6-Speed Manual Transmission"
    ),
    drivetrain="RWD",
    fuel_efficiency=FuelEfficiency(
        city_mpg=15,
        highway_mpg=24,
        combined_mpg=18
    ),
    dimensions=Dimensions(
        length=DimensionsUnit(188.5, "inches"),
        width=DimensionsUnit(75.4, "inches"),
        height=DimensionsUnit(54.3, "inches"),
        wheelbase=DimensionsUnit(107.1, "inches"),
        curb_weight=DimensionsUnit(3705, "lbs")
    ),
    features=Features(
        infotainment=["SYNC 3", "Apple CarPlay", "Bang & Olufsen Sound"],
        safety=["Blind Spot Monitoring", "Rear Cross Traffic Alert"],
        comfort=["Leather Seats", "Heated Steering Wheel"]
    ),
    color_options=["Red", "Black", "Yellow", "Silver"],
    price=Price(
        base_price=43000,
        currency="USD",
        msrp=45000,
        destination_fee=1200,
        total_price=46200
    ),
    warranty=Warranty(
        basic=WarrantyUnit(duration_years=3, miles=36000),
        powertrain=WarrantyUnit(duration_years=5, miles=60000),
        roadside_assistance=WarrantyUnit(duration_years=5, miles=60000)
    )
)

"""
car3 = CarItem(
    make = "Tesla",
    model = "Model 3",
    year = 2024,
    engine = {
        "engine_type": "Electric Motor",
        "fuel_type": "Electric",
        "displacement": "N/A",
        "horsepower": 283,
        "torque": {
            "torque_value": 307,
            "unit": "lb-ft",
            "rpm": "Instant"
        },
        "aspiration": "Electric"
    },
    transmission = {
        "transmission_type": "Single-Speed",
        "gears": 1,
        "description": "Single-Speed Fixed Gear"
    },
    drivetrain = "AWD",
    fuel_efficiency = {
        "city_mpg": 138,
        "highway_mpg": 126,
        "combined_mpg": 132
    },
    dimensions = {
        "length": {
            "unit_value": 184.8,
            "unit_name": "inches"
        },
        "width": {
            "unit_value": 72.8,
            "unit_name": "inches"
        },
        "height": {
            "unit_value": 56.4,
            "unit_name": "inches"
        },
        "wheelbase": {
            "unit_value": 113.2,
            "unit_name": "inches"
        },
        "curb_weight": {
            "unit_value": 4034,
            "unit_name": "lbs"
        }
    },
    features = {
        "infotainment": ["Tesla Theater", "Premium Sound", "Streaming Services"],
        "safety": ["Autopilot", "Automatic Emergency Braking"],
        "comfort": ["Glass Roof", "Heated Seats", "HEPA Air Filtration"]
    },
    color_options = ["Pearl White", "Solid Black", "Midnight Silver", "Deep Blue"],
    price = {
        "base_price": 40000,
        "currency": "USD",
        "msrp": 42990,
        "destination_fee": 1400,
        "total_price": 44390
    },
    warranty = {
        "basic": {
            "duration_years": 4,
            "miles": 50000
        },
        "powertrain": {
            "duration_years": 8,
            "miles": 120000
        },
        "roadside_assistance": {
            "duration_years": 4,
            "miles": 50000
        }
    }
)
"""
cars = {
    str(car1._id): car1,
    str(car2._id): car2
}