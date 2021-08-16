from flask_restful import Resource, reqparse

from models.hotel_models import HotelModel


class Hotels(Resource):
    def get(self):
        return {
            # Retorne todos os hotels dentro do query em HotelModel
            'hotels': [hotel.json() for hotel in HotelModel.query.all()]
        }


class Hotel(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('nome')
    arguments.add_argument('estrelas')
    arguments.add_argument('valor')

    def get(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found!'}, 404

    def post(self, id):
        if HotelModel.find_hotel(id):
            return {'message': f'Hotel - {id} already exists.'}, 400
        data = Hotel.arguments.parse_args()
        hotel_object = HotelModel(id, **data)
        hotel_object.save_hotel()
        return hotel_object.json(), 200

    def put(self, id):
        data = Hotel.arguments.parse_args()
        hotel = HotelModel.find_hotel(id)
        if hotel:
            hotel.update_hotel(**data)
            hotel.save_hotel()
            return hotel.json(), 200
        hotel_object = HotelModel(id, **data)
        hotel_object.save_hotel()
        return hotel_object.json(), 201

    def delete(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            hotel.delete_hotel()
            return {'message': 'Hotel deleted!'}
        return {'message': 'Hotel not found!'}
