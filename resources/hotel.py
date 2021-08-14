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
        'id': 'Hotel2',
        'nome': 'Hotel2',
        'estrelas': '4,5',
        'valor': '450,56',
    }, {
        'id': 'Hotel2',
        'nome': 'Hotel2',
        'estrelas': '4,5',
        'valor': '450,56',
    }, {
        'id': 'Hotel2',
        'nome': 'Hotel2',
        'estrelas': '4,5',
        'valor': '450,56',
    }
]


class Hotels(Resource):
    def get(self):
        return {'hotels': hotels}