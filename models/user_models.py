from sql_alchemy import db


class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    login = db.Column(db.String(40))
    password = db.Column(db.String(40))

    def __init__(self, name, login, password):
        self.name = name
        self.login = login
        self.password = password

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'login': self.login
        }

    @classmethod
    def find_user(cls, id):
        user = UserModel.query.filter_by(id=id).first()
        if user:
            return user
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.remove(self)
        db.session.commit()
