from flask_restful import Resource, reqparse
from models.user_models import UserModel


class User(Resource):
    def get(self, id):
        user = UserModel.query.filter_by(id=id)
        if user:
            return user.json()
        return {'message': 'User not found!'}, 404

    def delete(self, id):
        user = UserModel.find_user(id)
        if user:
            user.delete_user()
            return {'message': 'User been deleted!'}
        return {'message': 'User not found!'}, 404
