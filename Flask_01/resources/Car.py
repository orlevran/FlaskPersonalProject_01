from flask import request#, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import CarSchema, CarUpdateSchema
from cars_data import CarItem, cars

blp = Blueprint("cars", __name__, description="Operations on cars")

@blp.route("/cars/<string:car_id>")
class Car(MethodView):

    @blp.response(200, CarSchema)
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

    @blp.arguments(CarUpdateSchema)
    @blp.response(200, CarSchema)
    def put(self, car_data, car_id):
        try:
            #request_data = request.get_json()
            car = cars[car_id]
            car |= car_data
            cars[car_id] = car
            return car
        except KeyError as ke:
             abort(404, str(ke))

@blp.route("/cars")
class CarsList(MethodView):

    @blp.response(200, CarSchema(many=True))
    def get(self):
        return cars.values()
        #return {"cars" : list(cars.values())}
    
    @blp.arguments(CarSchema)
    @blp.response(201, CarSchema)
    def post(self, request_data):
        request_data = request.get_json()
        new_car = CarItem(
        make=request_data["make"],
        model=request_data["model"],
        year=request_data["year"],
        engine=request_data["engine"],
        transmission=request_data["transmission"],
        drivetrain=request_data["drivetrain"],
        fuel_efficiency=request_data["fuel_efficiency"],
        dimensions=request_data["dimensions"],
        features=request_data["features"],
        color_options=request_data["color_options"],
        price=request_data["price"],
        warranty=request_data["warranty"]
        )

        cars[str(new_car._id)] = {**new_car.to_dict()}
        return new_car
        #return jsonify(new_car.to_dict()), 201
