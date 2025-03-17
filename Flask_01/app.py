from flask import Flask, request, jsonify
from Car import *

app = Flask(__name__)

car1 = Car(
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

car2 = Car(
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

@app.route('/')
def home():
    return "Hello world"

@app.get("/cars")
def get_cars():
    try:
        return {"cars" : list(cars.values())}
    except Exception as e:
        return jsonify({"error": str(e)}), 400

#@app.get("/cars/<string:car_id>")
@app.get("/car")
def get_car():
    try:
        request_data = request.get_json()
        car_id=str(request_data["_id"])
        return cars[car_id], 201
    except KeyError as ke:
        return {"message" : "Car not found"}, 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.post("/cars")
def create_car():
    try:
        car_id = uuid.uuid4().hex

        request_data = request.get_json()
        new_car = Car(
        make=request_data["make"],
        model=request_data["model"],
        year=request_data["year"],
        engine=request_data["engine"],
        transmission=request_data["transmission"],
        fuel_efficiency=request_data["fuel_efficiency"],
        dimensions=request_data["dimensions"],
        features=request_data["features"],
        price=request_data["price"]
        )

        cars[str(car_id)] = {**new_car.to_dict()}
        return jsonify(new_car.to_dict()), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

