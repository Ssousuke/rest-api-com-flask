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
    arguments.add_argument('nome', type=str, required=True, help='The field nome cannot be left blank')
    arguments.add_argument('estrelas', type=float, required=True, help='The field estrelas cannot be left blank')
    arguments.add_argument('valor', type=float, required=True, help='The field valor cannot be left blank')

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
        try:
            hotel_object.save_hotel()
        except:
            return {'message': 'Internal server error, unable to save data.'}, 500
        return hotel_object.json(), 200

    def put(self, id):
        data = Hotel.arguments.parse_args()
        hotel = HotelModel.find_hotel(id)
        if hotel:
            hotel.update_hotel(**data)
            try:
                hotel.save_hotel()
            except:
                return {'message': 'Internal server error, unable to save data.'}, 500
            return hotel.json(), 200
        hotel_object = HotelModel(id, **data)
        hotel_object.save_hotel()
        return hotel_object.json(), 201

    def delete(self, id):
        hotel = HotelModel.find_hotel(id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'Internal server error, unable to delete data.'}, 500
            return {'message': 'Hotel deleted!'}
        return {'message': 'Hotel not found!'}
