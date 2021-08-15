from flask_restful import Resource, reqparse

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
    def get(self, id):
        for hotel in hotels:
            if hotel['id'] == id:
                return hotel
        return {'message': 'Hotel not found!'}, 404

    def post(self, id):
        arguments = reqparse.RequestParser()
        arguments.add_argument('nome')
        arguments.add_argument('estrelas')
        arguments.add_argument('valor')

        data = arguments.parse_args()

        new_hotel = {
            'id': id,
            'nome': data['nome'],
            'estrelas': data['estrelas'],
            'valor': data['valor'],
        }
        hotels.append(new_hotel)
        return new_hotel, 200

    def put(self, id):
        pass

    def delete(self, id):
        pass
