class HotelModel:
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
