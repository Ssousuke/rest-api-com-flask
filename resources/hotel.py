from flask_restful import Resource

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

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
