from sql_alchemy import db


class HotelModel(db.Model):
    __tablename__ = 'hotels'
    id = db.Column(db.String, primary_key=True)
    nome = db.Column(db.String(80))
    estrelas = db.Column(db.Float(precision=1))
    valor = db.Column(db.Float(precision=2))

    def __init__(self, id, nome, estrelas, valor):
        self.id = id
        self.nome = nome
        self.estrelas = estrelas
        self.valor = valor

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'valor': self.valor
        }
