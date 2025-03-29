from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from cars_data import cars, CarItem

blp = Blueprint("cars", __name__, description="Operations on cars")

@blp.route("/cars/<string:car_id>")
class Car(MethodView):
    def get(self, car_id):
        try:
            return cars[car_id], 200
        except KeyError:
            abort(404, message="Car not found")
    
    def delete(self, car_id):
        try:
            del cars[car_id]
            return {"message" : f"Car {car_id} deleted"}
        except KeyError:
            abort(404, message="Car not found")

    def put(self, car_id):
        try:
            request_data = request.get_json()
            car = cars[car_id]
            car |= request_data
            cars[car_id] = car
            return car
        except KeyError as ke:
             abort(404, str(ke))

@blp.route("/cars")
class CarsList(MethodView):
    def get(self):
        return {"cars" : list(cars.values())}
    
    def post(self):
        request_data = request.get_json()
        new_car = CarItem(
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

        cars[str(new_car._id)] = {**new_car.to_dict()}
        return jsonify(new_car.to_dict()), 201
