from flask_restful import Resource, reqparse
from models.user import UserModel
class Users(Resource):
    def get(self):
        return {'users': [user.json() for user in UserModel.query.all()]}

class User(Resource):   
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome', type=str, required=True, help="This field 'nome' cannot be left blank")
    argumentos.add_argument('email', type=str, required=True, help="This field 'email' cannot be left blank")
    argumentos.add_argument('telefone', type=int)

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
        try:
            user.save_user()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return user.json()

    def put(self, id):
        dados = User.argumentos.parse_args()
        user_encontrado = UserModel.find_user(id)
        if user_encontrado:
            user_encontrado.update_user(**dados)
            user_encontrado.save_user()
            return user_encontrado.json(), 200 #OK
        user = UserModel(id, **dados)
        try:
            user.save_user()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return user.json(), 201 #created

    def delete(self, id):
        user = UserModel.find_user(id)
        if user:
            try:
                user.delete_user()
            except:
                return {'message': 'An internal error ocurred trying to delete user.'}, 500
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404