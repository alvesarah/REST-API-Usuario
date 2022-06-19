from flask_restful import Resource, reqparse
from models.user import UserModel
class Users(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

class User(Resource):   
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('telefone')

    def get(self, id):
        user = UserModel.find_user(id)
        if user:
            return user.json()
        return {'message': 'User not found.'}, 404

    def post(self, id):
        if UserModel.find_user(id):
            return {"message": "User id '{}' already exists.".format(id)}, 400

        dados = User.argumentos.parse_args()
        user = UserModel(id, **dados)
        user.save_user()
        return user.json()

    def put(self, id):
        dados = User.argumentos.parse_args()
        user_encontrado = UserModel.find_user(id)
        if user_encontrado:
            user_encontrado.update_user(**dados)
            user_encontrado.save_user()
            return user_encontrado.json(), 200 #OK
        user = UserModel(id, **dados)
        user.save_user()
        return user.json(), 201 #created

    def delete(self, id):
        user = UserModel.find_user(id)
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404