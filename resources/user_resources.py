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
            try:
                user.delete_user()
            except:
                return {'message': 'Internal server error, unable to delete data.'}, 500
            return {'message': 'User been deleted!'}
        return {'message': 'User not found!'}, 404


class UserRegister(Resource):
    def post(self):
        arguments = reqparse.RequestParser()
        arguments.add_argument('login', type=str, required=True, help='the login field is cannot be left blank.')
        arguments.add_argument('password', type=str, required=True, help='the password field is cannot be left blank.')

        data = arguments.parse_args()

        if UserModel.find_by_login(data['login']):
            return {'message': f"The login {data['login']} already exists."}
        user = UserModel(**data)
        user.save_user()
        return {'message': 'User created successfully.'}
