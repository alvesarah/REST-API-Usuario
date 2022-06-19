from flask_restful import Resource, reqparse
from models.user import UserModel
class Users(Resource):
    def get(self):
        return {'users': users}

class User(Resource):   
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('email')
    argumentos.add_argument('telefone')

    def get(self, id):
        user = User.find_user(id)
        if user:
            return user
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
        user_objeto = UserModel(id, **dados)
        novo_user = user_objeto.json()

        user = User.find_user(id)
        if user:
            user.update(novo_user)
            return novo_user, 200
        users.append(novo_user)
        return novo_user, 201

    def delete(self, id):
        global users
        users = [user for user in users if user['id'] != id]
        return {'messagem': 'User deleted.'}