from flask_restful import Resource, reqparse

from models.hotel_models import HotelModel

hotels = [
    {
        'id': 'Hotel1',
        'nome': 'Hotel1',
        'estrelas': '4,5',
        'valor': '450,56',
    }, {
        'id': 'Hotel2',
        'nome': 'Hotel2',
        'estrelas': '4,5',
        'valor': '450,56',
    }, {
        'id': 'Hotel3',
        'nome': 'Hotel3',
        'estrelas': '4,5',
        'valor': '450,56',
    }, {
        'id': 'Hotel4',
        'nome': 'Hotel4',
        'estrelas': '4,5',
        'valor': '450,56',
    }, {
        'id': 'Hotel5',
        'nome': 'Hotel5',
        'estrelas': '4,5',
        'valor': '450,56',
    }
]


class Hotels(Resource):
    def get(self):
        return {'hotels': hotels}


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
        hotel_object = HotelModel(id, **data)
        new_hotel = hotel_object.json()
        hotel = Hotel.find_hotel(id)
        if hotel:
            hotel.update(new_hotel)
            return new_hotel, 200
        hotels.append(new_hotel)
        return new_hotel, 201

    def delete(self, id):
        global hotels
        hotels = [hotel for hotel in hotels if hotel['id'] != id]
        return {'message': 'Hotel deleted!'}
