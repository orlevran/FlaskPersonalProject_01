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
            car = cars[car_id]
            for key, value in car_data.items():
                if hasattr(car, key):
                    setattr(car, key, value)
            cars[car_id] = car
            return car
        except KeyError as ke:
            abort(404, str(ke))

@blp.route("/cars")
class CarsList(MethodView):

    @blp.response(200, CarSchema(many=True))
    def get(self):
        return [car.to_dict() for car in cars.values()]
        
    @blp.arguments(CarSchema)
    @blp.response(201, CarSchema)
    def post(self, request_data):
        new_car = CarItem.from_dict(request_data)
        cars[str(new_car._id)] = new_car
        return new_car